from sqlalchemy.orm import Query
from sqlalchemy.orm.session import Session
from werkzeug.security import generate_password_hash, check_password_hash

from .db import db
from .models import User, Post


def get_user_by_id(id):
    query: Query = User.query
    user = query.get(id)
    return user


def get_user_by_username(username):
    query: Query = User.query
    user = query.filter_by(username=username).first()
    return user


def create_user(username, password):
    session: Session = db.create_scoped_session()
    session.add(User(username, generate_password_hash(password)))
    session.commit()
    session.close()


def authenticate_user(username, password):
    user = get_user_by_username(username)
    if user and check_password_hash(user.password, password):
        return user


def get_all_posts():
    query: Query = Post.query
    return query.all()


def create_post(title, body, user_id):
    session: Session = db.create_scoped_session()
    session.add(Post(title, body, user_id))
    session.commit()
    session.close()


def get_post_by_id(post_id):
    query: Query = Post.query
    post = query.get(post_id)
    return post


def get_post_by_id_and_author(post_id, user_id):
    post = get_post_by_id(post_id)
    return post if post.author_id == user_id else None


def update_post(post_id, new_title, new_body):
    session: Session = db.create_scoped_session()
    post = session.query(Post).get(post_id)
    post.title = new_title
    post.body = new_body
    session.commit()
    session.close()


def delete_post(post_id):
    session: Session = db.create_scoped_session()
    post = session.query(Post).get(post_id)
    session.delete(post)
    session.commit()
    session.close()
