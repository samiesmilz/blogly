""" Seed file to make ssample data for the database. """

from app import app
from models import db, User, Post, PostTag, Tag

# Create all tables

db.engine.execute('DROP SCHEMA public CASCADE; CREATE SCHEMA public;')
db.create_all()

# Sample data for users
jinna = User(
    first_name="Jinna",
    last_name="Ray",
    image_url="https://images.pexels.com/photos/415829/pexels-photo-415829.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
)

trina = User(
    first_name="Trina",
    last_name="Best",
    image_url="https://mymodernmet.com/wp/wp-content/uploads/2019/09/100k-ai-faces-7.jpg"
)

brave = User(
    first_name="Brave",
    last_name="Miles",
    image_url="https://mymodernmet.com/wp/wp-content/uploads/2019/09/100k-ai-faces-4.jpg"
)

nora = User(
    first_name="Nora",
    last_name="Shelbie",
    image_url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpetapixel.com%2Fassets%2Fuploads%2F2019%2F02%2FaYmax6O3.jpg&f=1&nofb=1&ipt=c0fbc2dd38a0c0f44e2dcd31a28a1a194314b7aea84db810013542732f9bffef&ipo=images"
)

nina = User(
    first_name="Nina",
    last_name="Winson",
    image_url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2F1.img-dpreview.com%2Ffiles%2Fp%2FTS560x560~forums%2F63132016%2F2a1e59e12f4543bea10f2385259c81cf&f=1&nofb=1&ipt=4a537ae9e815ca98d6e9bf5955cd70fc97fa956e268e78c7ac4cab10805e64b3&ipo=images"
)

praise = User(
    first_name="Praise",
    last_name="Onan",
    image_url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpetapixel.com%2Fassets%2Fuploads%2F2019%2F09%2F6-1.jpg&f=1&nofb=1&ipt=c74519421b9f574dc870544ef6d4afcf6b194bea50cb1056167b5c539646105a&ipo=images"
)

# Add sample users to the database using User instances
db.session.add_all([jinna, trina, brave, nora, nina, praise])

# Commit the changes to the database
db.session.commit()


# sample data for posts

post1 = Post(
    title="Elevate Your Web Design with Bootstrap",
    content="In the fast-paced world of web development, having a responsive and visually appealing design is paramount. Explore Bootstrap, a front-end framework that empowers developers to create stunning, mobile-friendly websites effortlessly.",
    user_id=3
)

post2 = Post(
    title="PostgreSQL Demystified",
    content="In the realm of database management, PostgreSQL stands out as a powerful and versatile option. This open-source relational database system not only excels in handling complex queries but also offers advanced features like support for JSON data, full-text search, and extensibility.",
    user_id=4
)

post3 = Post(
    title="Flask: A Lightweight Python Framework for Web Development",
    content="From routing to templating, Flask empowers developers to create web applications with ease. Whether you're a solo developer working on a small project or part of a larger team, Flask's extensibility and modular design make it a go-to choice for building scalable and maintainable web applications.",
    user_id=1
)

# Add all sample posts in the database tables.
db.session.add_all([post1, post2, post3])
db.session.commit()


# Sample data for more tags
python_tag = Tag(name="Python")
web_dev_tag = Tag(name="Web Development")
database_tag = Tag(name="Database")
flask_tag = Tag(name="Flask")
bootstrap_tag = Tag(name="Bootstrap")

# Add more sample tags to the database
db.session.add_all(
    [python_tag, web_dev_tag, database_tag, flask_tag, bootstrap_tag])
db.session.commit()

# Sample data for more posts
post4 = Post(
    title="Mastering Python Basics",
    content="Build a strong foundation in Python programming by mastering the basics. From variables and data types to control flow and functions, this comprehensive guide will help you become proficient in Python.",
    user_id=6
)

post5 = Post(
    title="The Power of Web Development",
    content="Explore the dynamic world of web development and discover how it shapes the digital landscape. From front-end frameworks like Bootstrap to back-end technologies, this journey will unveil the potential of web development.",
    user_id=5
)

post6 = Post(
    title="Diving Into Databases with SQL",
    content="Unlock the secrets of SQL and databases. Learn how to design, query, and optimize databases to store and retrieve data efficiently. Whether you're a beginner or an experienced developer, this guide has something for everyone.",
    user_id=2
)

# Add more sample posts to the database
db.session.add_all([post4, post5, post6])
db.session.commit()

# Create associations between posts and tags
post1.tags.extend([python_tag, web_dev_tag])
post2.tags.extend([database_tag, python_tag])
post3.tags.append(flask_tag)
post4.tags.append(python_tag)
post5.tags.extend([web_dev_tag, bootstrap_tag])
post6.tags.extend([database_tag, python_tag])

# Commit the changes
db.session.commit()
