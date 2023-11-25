"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

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
