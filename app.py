"""Blogly application."""

from flask import request
from flask import Flask, redirect, flash, render_template, request, abort
from models import db, connect_db, User, Post

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


# Routes for posts

@app.route("/posts")
def get_posts():
    """ Retrieve and show all posts in database """
    posts = Post.query.all()
    return render_template("posts.html", posts=posts)


@app.route("/users/<int:user_id>/posts/new")
def show_new_post_form(user_id):
    """ Display form to create a new post for user"""
    user = User.query.get(user_id)
    return render_template("add_post.html", user=user)


@app.route("/users/<int:user_id>/posts/new", methods=['POST'])
def create_post(user_id):

    title = request.form.get("title")
    content = request.form.get("content")
    post = Post(title=title, content=content, user_id=user_id)

    db.session.add(post)
    db.session.commit()

    return redirect(f"/users/{user_id}")


@app.route("/posts/<int:post_id>")
def show_post(post_id):
    """ Display edit post form """
    post = Post.query.get(post_id)
    return render_template("post.html", post=post)


@app.route("/posts/<int:post_id>/edit")
def edit_post_form(post_id):
    """ Display edit post form """
    post = Post.query.get(post_id)
    return render_template("edit_post.html", post=post)


@app.route("/posts/<int:post_id>/edit", methods=['POST'])
def update_post(post_id):
    """ Edit post in database """

    post = Post.query.get(post_id)
    post.title = request.form.get("title")
    post.content = request.form.get("content")

    db.session.add(post)
    db.session.commit()

    return redirect("/posts")


@app.route("/posts/<int:post_id>/delete", methods=['POST'])
def delete_post(post_id):
    """ Delete user post"""

    post = Post.query.get(post_id)

    if post:
        db.session.delete(post)
        db.session.commit()
        return redirect("/posts")
    else:
        abort(404)
