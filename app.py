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
@app.route("/recipes")
def recipes():
    recipes = list(mongo.db.recipes.find())
    categories = mongo.db.categories.find()
    for recipe in recipes:
        category_name = mongo.db.categories.find_one(
            {"_id": ObjectId(recipe["category_id"])})["category_name"]
        recipe["category_id"] = category_name
    return render_template(
        "recipes.html", recipes=recipes, categories=categories)


@app.route("/my_recipes", methods=["GET", "POST"])
def my_recipes():
    if request.method == "POST":
        my_recipes = {
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
        mongo.db.my_recipes.insert_one(my_recipes)
        flash("Recipe Successfully Added")
    return render_template("my_recipes.html")


@app.route("/favourites")
def favourites():
    return render_template("favourites.html")


@app.route("/login", methods=["GET", "POST"])
def login():
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
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            # username doesnt exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # checks if user already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # tells user already exists and directs them to registration page
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "my_recipes": [],
            "favourites": [],
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # puts the new user into sessions cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successfull!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
            