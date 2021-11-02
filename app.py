import os
from flask import (
  Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_paginate import Pagination, get_page_args
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


def get_recipes(recipes, offset=0, per_page=12):
    """
    Give pagination information about recipes
    """
    recipes = list(mongo.db.recipes.find())
    return recipes[offset: offset + per_page]


@app.route("/")
@app.route("/home")
def home():
    """
    First page to load when user registers to site
    """
    quotes = list(mongo.db.quotes.find())
    return render_template("home.html", quotes=quotes)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    checks if user is in DB, if not then redirects to register page
    """
    if request.method == "POST":
        # checks if user already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # tells user already exists and directs them to registration page
            flash("Username already exists")
            return redirect(url_for("register"))

        new_user = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "favourites": []
        }
        mongo.db.users.insert_one(new_user)

        # puts the new user into sessions cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successfull!")
        return redirect(url_for("recipes", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    checks if user has username and passowrd in DB.
    """
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("profile", user=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            # username doesnt exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<user>", methods=["GET", "POST"])
def profile(user):
    """
    grabs user from DB and redirects them to profile page after login.
    """
    if "user" in session:
        user = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        my_recipes = list(mongo.db.recipes.find(
            {"created_by": session["user"]}))
    else:
        flash("Sorry, you are unable to do this, please log in")
        return redirect(url_for("login"))
    return render_template("profile.html", user=user, my_recipes=my_recipes)


@app.route("/logout")
def logout():
    """
    logs user out of account, clears session cookie
    """
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


def get_search_recipes(offset=0, per_page=12):
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return recipes[offset: offset + per_page]


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    searches DB for recipes that user types into search field.
    """
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    # Pagination
    # pylint: disable=unbalanced-tuple-unpacking
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    # pylint: enable=unbalanced-tuple-unpacking
    total = len(recipes)
    pagination_recipes = get_search_recipes(offset=offset, per_page=12)
    pagination = Pagination(page=page, per_page=12, total=total)
    categories = mongo.db.categories.find()
    flash("Here is a list of recipes you searched for")
    return render_template(
        "recipes.html", recipes=pagination_recipes, categories=categories,
        page=page, per_page=per_page, pagination=pagination)


@app.route("/recipes")
def recipes():
    """
    checks for recipes on DB and renders them on HTML recipe page.
    """
    recipes = list(mongo.db.recipes.find())
    # Pagination
    # pylint: disable=unbalanced-tuple-unpacking
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    # pylint: enable=unbalanced-tuple-unpacking
    total = len(recipes)
    pagination_recipes = get_recipes(recipes, offset=offset, per_page=12)
    pagination = Pagination(page=page, per_page=12, total=total)
    categories = mongo.db.categories.find()
    if "user" in session:
        user = mongo.db.users.find_one({"username": session["user"]})
    else:
        user = False
    return render_template(
        "recipes.html", recipes=pagination_recipes, categories=categories,
        user=user, page=page, per_page=per_page, pagination=pagination)


@app.route("/full_recipes/<recipe_id>")
def full_recipes(recipe_id):
    """
    gets full recipe from db to render on site
    """
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    try:
        category_name = mongo.db.categories.find_one(
            {"_id": ObjectId(recipe["category_id"])})["category_name"]
        recipe["category_id"] = category_name
    except BaseException:
        recipe["category_id"] = "undefined"
    return render_template("full_recipes.html", recipe=recipe)


@app.route("/add_recipes", methods=["GET", "POST"])
def add_recipes():
    """
    adds user recipes into DB, renders them to profile page and recipe page.
    """
    if "user" in session:
        if request.method == "POST":
            add_recipes = {
                "ingredients": request.form.get("ingredients").splitlines(),
                "method": request.form.get("method").splitlines(),
                "prep_time": request.form.get("prep_time"),
                "name": request.form.get("name"),
                "image": request.form.get("image"),
                "cook_time": request.form.get("cook_time"),
                "created_by": session["user"]
            }
            mongo.db.recipes.insert_one(add_recipes)
            flash("Recipe Successfully Added")
    else:
        flash("Sorry, you are unable to do this, please log in")
        return redirect(url_for("login"))
    return render_template("add_recipes.html")


@app.route("/edit_recipes/<recipe_id>", methods=["GET", "POST"])
def edit_recipes(recipe_id):
    """
    edits user recipes into DB.
    """
    if "user" in session:
        if request.method == "POST":
            change_recipes = {
                "ingredients": request.form.get("ingredients").splitlines(),
                "method": request.form.get("method").splitlines(),
                "prep_time": request.form.get("prep_time"),
                "name": request.form.get("name"),
                "image": request.form.get("image"),
                "image_alt": request.form.get("image_alt"),
                "cook_time": request.form.get("cook_time"),
                "created_by": session["user"]
            }
            mongo.db.recipes.update(
                {"_id": ObjectId(recipe_id)}, change_recipes)
            flash("Recipe Successfully update")
        recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    else:
        flash("Sorry, you are unable to do this, please log in")
        return redirect(url_for("login"))
    return render_template("edit_recipes.html", recipe=recipe)


@app.route("/delete_recipes/<recipe_id>")
def delete_recipes(recipe_id):
    """
    deletes recipes from database
    """
    if "user" in session:
        mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
        flash("Recipe Successfully Deleted")
    else:
        flash("Sorry, you are unable to do this, please log in")
        return redirect(url_for("Login"))
    return redirect(url_for("recipes"))


@app.route("/favourites")
def favourites():
    """
    adds recipes to favourites
    """
    recipes = list(mongo.db.recipes.find())
    categories = mongo.db.categories.find()
    if "user" in session:
        user = mongo.db.users.find_one({"username": session["user"]})
    else:
        user = False
    return render_template("favourites.html", recipes=recipes, categories=categories, user=user)


@app.route("/recipe/add_to_favourites/<recipe_id>")
def save_to_favourites(recipe_id):
    """
    add recipes into favourites collection in DB.
    """
    if "user" in session:
        user = mongo.db.users.find_one(
            {"username": session["user"]})["_id"]
        mongo.db.users.update_one(
            {"_id": ObjectId(user)},
            {"$push": {"favourites": ObjectId(recipe_id)}})
        flash("recipe added to favourites")
    else:
        flash("Sorry, you are unable to do this, please log in")
        return redirect(url_for("login"))
    return redirect(url_for("recipes"))


@app.route("/recipe/delete_from_favourites/<recipe_id>")
def delete_from_favourites(recipe_id):
    """
    deletes recipes from favourites collection in DB and favourites HTML page.
    """
    if "user" in session:
        user = mongo.db.users.find_one(
            {"username": session["user"]})["_id"]
        mongo.db.users.update_one(
            {"_id": ObjectId(user)},
            {"$pull": {"favourites": ObjectId(recipe_id)}})
        flash("recipe removed from favourites")
    else:
        return redirect(url_for("login"))
    return redirect(url_for("recipes"))


@app.route("/recipe/delete_from_favourites_page/<recipe_id>")
def delete_from_favourites_page(recipe_id):
    """
    deletes recipes from favourites collection in DB and favourites HTML page.
    """
    if "user" in session:
        user = mongo.db.users.find_one(
            {"username": session["user"]})["_id"]
        mongo.db.users.update_one(
            {"_id": ObjectId(user)},
            {"$pull": {"favourites": ObjectId(recipe_id)}})
    else:
        return redirect(url_for("login"))
    return redirect(url_for("favourites"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
                     