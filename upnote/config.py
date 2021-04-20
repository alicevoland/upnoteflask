from dotenv import load_dotenv
load_dotenv()

from os import environ

SECRET_KEY = environ.get('SECRET_KEY')