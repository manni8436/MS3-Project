import os
from flask import (
  Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


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

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # puts the new user into sessions cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successfull!")
        return redirect(url_for("home", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    checks if user has username in DB.
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
    # grab the session user's username from db
    user = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    my_recipes = list(mongo.db.recipes.find(
        {"created_by": session["user"]}))
    return render_template("profile.html", user=user, my_recipes=my_recipes)


@app.route("/logout")
def logout():
    """
    logs user out of account, clears session cookie
    """
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    searches DB for recipes that user types into search field.
    """
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    flash("Here is a list of recipes you searched for")
    return render_template("recipes.html", recipes=recipes)


@app.route("/recipes")
def recipes():
    """
    checks for recipes on DB and renders them on HTML recipe page.
    """
    recipes = list(mongo.db.recipes.find())
    favourites = list(mongo.db.favourites.find())
    categories = mongo.db.categories.find()
    return render_template(
        "recipes.html", recipes=recipes, categories=categories, favourites=favourites)


@app.route("/add_recipes", methods=["GET", "POST"])
def add_recipes():
    """
    adds user recipes into DB, renders them to profile page and recipe page.
    """
    if request.method == "POST":
        add_recipes = {
            "ingredients": request.form.get("ingredients"),
            "method": request.form.get("method"),
            "prep_time": request.form.get("prep_time"),
            "name": request.form.get("name"),
            "image": request.form.get("image"),
            "image_alt": request.form.get("image_alt"),
            "cook_time": request.form.get("cook_time"),
            "favourites": request.form.get("favourites"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(add_recipes)
        flash("Recipe Successfully Added")
    return render_template("add_recipes.html")


@app.route("/edit_recipes/<recipe_id>", methods=["GET", "POST"])
def edit_recipes(recipe_id):
    """
    edits user recipes into DB.
    """
    if request.method == "POST":
        edit_recipes = {
            "ingredients": request.form.get("ingredients"),
            "method": request.form.get("method"),
            "prep_time": request.form.get("prep_time"),
            "name": request.form.get("name"),
            "image": request.form.get("image"),
            "image_alt": request.form.get("image_alt"),
            "cook_time": request.form.get("cook_time"),
            "my_recipes": request.form.get("my_recipes"),
            "favourites": request.form.get("favourites"),
            "created_by": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, edit_recipes) 
        flash("Recipe Successfully update")
    return render_template("edit_recipes.html")


@app.route("/delete_recipes/<recipe_id>")
def delete_recipes(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("recipes"))


@app.route("/favourites")
def favourites():
    user = list(mongo.db.favourites.find(
        {"$and": [{"username": {'$eq': session["user"]}}]}))
    favourites_list = []
    for i in user:
        favourites_list.append(mongo.db.recipes.find_one(
            {"_id": ObjectId(i["recipe_name"])}))
    return render_template("favourites.html", favourites_list=favourites_list)


@app.route("/recipe/add_to_favourites/<recipe_id>", methods=["GET", "POST"])
def save_to_favourites(recipe_id):
    """
    add recipes into favourites collection in DB.
    """
    if session["user"]:
        data = {
            "recipe_name": ObjectId(recipe_id),
            "username": session["user"],
        }
    mongo.db.favourites.insert_one(data)
    return redirect(url_for("recipes"))


@app.route("/recipe/delete_from_favourites/<favourite_id>")
def delete_from_favourites(favourite_id):
    """
    deltes recipes into favourites collection in DB and from favourites HTML page.
    """
    if session["user"]:
        mongo.db.favourites.remove({"recipe_name": ObjectId(favourite_id)})
        return redirect(url_for("favourites"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
                     