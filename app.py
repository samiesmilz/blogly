"""Blogly application."""

from flask import request
from flask import Flask, redirect, flash, render_template, request, abort
from models import db, connect_db, User, Post, Tag, PostTag
from datetime import datetime

app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = 'devwoof0700'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)


@app.route("/")
def home():
    """ Got to homepage """
    posts = Post.query.all()
    return render_template("index.html", posts=posts)


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


@app.route("/posts/<int:post_id>/edit", methods=['GET', 'POST'])
def edit_post(post_id):
    """ View and update a post"""
    # Fetch the post
    post = Post.query.get(post_id)

    if request.method == 'POST':
        # Update post details
        post.title = request.form.get("title")
        post.content = request.form.get("content")

        # Get the list of tag IDs from the form
        selected_tag_ids = list(map(int, request.form.getlist('tags')))

        # Clear existing tags
        post.tags.clear()

        # Add selected tags
        post.tags.extend(Tag.query.filter(Tag.id.in_(selected_tag_ids)))

        # Commit changes to the database
        db.session.commit()

        # Redirect to the post details page
        return redirect(f"/posts/{post.id}")

    # Fetch all tags for rendering the form
    tags = Tag.query.all()

    return render_template("edit_post.html", post=post, tags=tags)


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


# Routes for tags

@app.route("/tags")
def show_all_tags():
    """Display all available tags"""
    tags = Tag.query.all()
    return render_template("tags.html", tags=tags)


@app.route("/tags/<int:id>")
def show_tag(id):
    """ Show individual tag """
    tag = Tag.query.get(id)
    return render_template("tag.html", tag=tag)


@app.route("/tags/<int:id>/edit", methods=['GET', 'POST'])
def edit_tag(id):
    """ Edit tag """
    tag = Tag.query.get(id)

    if request.method == 'POST':
        tag_name = request.form.get("tag_name")

        if tag_name:
            tag.name = tag_name

            # Get the list of post IDs from the form
            selected_post_ids = list(map(int, request.form.getlist('posts')))

            # Update tag associations with posts
            tag.posts = [
                post for post in tag.posts if post.id in selected_post_ids]

            db.session.add(tag)
            db.session.commit()

            return redirect(f"/tags/{id}")

    return render_template("edit_tag.html", tag=tag)


@app.route("/tags/<int:id>/delete")
def delete_tag(id):
    """ Delete tag """
    tag = Tag.query.get(id)
    db.session.delete(tag)
    db.session.commit()
    return redirect("/tags")


@app.route("/tags/new", methods=['GET', 'POST'])
def add_tag():
    """ Add a new tag """
    tags = Tag.query.all()
    if request.method == 'POST':
        tag = request.form.get("tag_name")
        if tag:
            new_tag = Tag(name=tag)
            db.session.add(new_tag)
            db.session.commit()
            return redirect("/tags/new")
        else:
            return redirect("/tags/new")

    return render_template("add_tag.html", tags=tags)
