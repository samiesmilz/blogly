"""Blogly application."""

from flask import request
from flask import Flask, redirect, flash, render_template, request, abort
from models import db, connect_db, User

app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = 'devwoof0700'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)


@app.route("/")
def home():
    """ Got to homepage """
    return render_template("index.html")


@app.route("/users")
def get_users():
    """ Get and display a list of all users """
    users = User.query.all()
    return render_template("users.html", users=users)


@app.route("/users/new")
def create_user_form():
    """ Create new user form """
    return render_template("form.html")


@app.route("/users/new", methods=['POST'])
def create_user():
    """ Send new user data to database """
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    image_url = request.form.get("image_url")

    new_user = User(first_name=first_name,
                    last_name=last_name, image_url=image_url)

    db.session.add(new_user)
    db.session.commit()
    return redirect("/users")


@app.route("/users/<int:user_id>")
def get_user(user_id):
    """ Get and display a single user profile """
    user = User.query.get_or_404(user_id)
    return render_template("user.html", user=user)


@app.route("/users/<int:user_id>/edit")
def edit_user(user_id):
    """ Unlock user form for editing profile """
    user = User.query.get(user_id)
    return render_template("edit_user.html", user=user)


@app.route("/users/<int:user_id>/edit", methods=["POST"])
def update_user(user_id):
    """ Post the current user profile edits in the database """

    user = User.query.get_or_404(user_id)

    # Update user attributes based on form data
    user.first_name = request.form.get("first_name")
    user.last_name = request.form.get("last_name")
    user.image_url = request.form.get("image_url")

    # Commit the changes to the database
    db.session.commit()

    return redirect(f"/users/{user_id}")


@app.route("/users/<int:user_id>/delete")
def delete_user(user_id):
    """ Delete a user from the database """
    user = User.query.get(user_id)

    if user:
        db.session.delete(user)
        db.session.commit()
        return redirect("/users")
    else:
        abort(404)
