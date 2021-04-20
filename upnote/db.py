from flask import g, current_app
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
#
def db_init_app(app):
    db.init_app(app)
    migrate = Migrate(app, db)
    db.create_all(app=app)
#     db = get_db()
#     db.init_app(app)
#     Migrate(app, db)
#
#
# # def get_db():
# #     return _db
#
# #
# #
# def get_db():
#     if 'db' not in g:
#         g.db = SQLAlchemy()
#
#     return g.db
#
# # import sqlite3
#
# import click
# from flask import current_app, g
# from flask.cli import with_appcontext


#
#
# def close_db(e=None):
#     db = g.pop('db', None)
#
#     if db is not None:
#         db.close()
# #
# def init_db():
#     db = get_db()
#     db.init_app(current_app)

#
#
# @click.command('init-db')
# @with_appcontext
# def init_db_command():
#     """Clear the existing data and create new tables."""
#     init_db()
#     click.echo('Initialized the database.')
#
# def init_app(app):
#     app.teardown_appcontext(close_db)
#     app.cli.add_command(init_db_command)
