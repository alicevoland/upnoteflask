from dotenv import load_dotenv
from os import environ

load_dotenv()


class Config(object):
    SECRET_KEY = environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = environ['DATABASE_URL']
    # Fix heroku naming
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
    print('upnote.config: SQLALCHEMY_DATABASE_URI', SQLALCHEMY_DATABASE_URI)
    if SQLALCHEMY_DATABASE_URI.startswith('postgres:'):
        print('update postres => postresql')
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace('postgres:', 'postgresql:')

    SQLALCHEMY_TRACK_MODIFICATIONS = False
