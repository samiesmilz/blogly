"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Make database
db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


class User(db.Model):
    __tablename__ = 'users'

    def __repr__(self):
        user = self
        return f"id={user.id} <first_name={user.first_name} last_name={user.last_name}>"

    # Properties
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False,
                           unique=False, default='New User')
    last_name = db. Column(db.String(50), nullable=True, unique=False)
    image_url = db.Column(db.String(255), nullable=True, unique=False)

    def greet(self):
        """ Greet user by first_name """
        return f"Hi {self.first_name}"

    def edit_profile(self, first_name, last_name, image_url):
        self.first_name = first_name
        self.last_name = last_name
        self.image_url = image_url


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship("User", backref="posts")

    tags = db.relationship("Tag", secondary='posttags',
                           backref='posts')

    def __repr__(self):
        return f"< Post Id: {self.id} Post-Title: {self.title} Created-At: {self.created_at} >"

    def last_updated(post):
        """Format datetime to be user friendly"""
        dt_object = post.created_at

        # Format the datetime object as a string with a desired format
        formatted_time = dt_object.strftime("%B %d, %Y %I:%M %p")

        return formatted_time


class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), unique=True)


class PostTag(db.Model):
    __tablename__ = "posttags"

    post_id = db.Column(db.Integer, db.ForeignKey(
        'posts.id'), nullable=False, primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey(
        'tags.id'), nullable=False, primary_key=True)
