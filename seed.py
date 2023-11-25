from app import create_app, db
from models import User

# Create an app with the same configuration as your main app
app = create_app()

# Connect to the database
with app.app_context():
    # Create tables (if they don't exist)
    db.create_all()

    # Add sample data
    sample_user1 = User(first_name='Jinna', last_name='Ray',
                        image_url='https://images.pexels.com/photos/415829/pexels-photo-415829.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2')
    sample_user2 = User(first_name='Jane', last_name='Doe',
                        image_url='https://mymodernmet.com/wp/wp-content/uploads/2019/09/100k-ai-faces-5.jpg')

    # Add and commit the sample users to the database
    db.session.add_all([sample_user1, sample_user2])
    db.session.commit()

    print("Sample data added to the database.")
