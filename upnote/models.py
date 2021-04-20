# print('models.py: my db is ' + str(db))
from datetime import datetime

from sqlalchemy import String

from upnote.db import db


# Base = declarative_base()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    password = db.Column(String())

    def __init__(self, username, password):
        self.password = password
        self.username = username

    def __repr__(self):
        return f"<User {self.username}>"


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    body = db.Column(db.Text())
    created = db.Column(db.DateTime())
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, title, body, author_id):
        self.title = title
        self.body = body
        self.author_id = author_id
        self.created = datetime.now()

    def __repr__(self):
        return f"<Post {self.title} by author_id={self.author_id}>"
