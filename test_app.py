import unittest
from flask import Flask
from flask.testing import FlaskClient
from models import db, User
from app import app, connect_db


class BloglyAppTestCase(unittest.TestCase):
    def setUp(self):
        """Set up the test environment"""
        app.config['TESTING'] = True
        # Use an in-memory SQLite database for testing
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.client = app.test_client()
        connect_db(app)
        db.create_all()

    def tearDown(self):
        """Clean up after the test"""
        db.session.remove()
        db.drop_all()

    def test_home(self):
        """Test the home route"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_get_users(self):
        """Test the get_users route"""
        # Add a user for testing
        user = User(first_name='John', last_name='Doe',
                    image_url='example.jpg')
        db.session.add(user)
        db.session.commit()

        response = self.client.get('/users')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'John', response.data)

    def test_create_user(self):
        """Test the create_user route"""
        response = self.client.post(
            '/users/new', data={'first_name': 'Jane', 'last_name': 'Doe', 'image_url': 'example.jpg'})
        self.assertEqual(response.status_code, 302)  # 302 indicates a redirect

        # Check if the user was added to the database
        user = User.query.filter_by(first_name='Jane').first()
        self.assertIsNotNone(user)

    # Add more tests for other routes...


if __name__ == '__main__':
    unittest.main()
