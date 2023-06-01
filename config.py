import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    DEBUG = os.environ.get("DEBUG")
    DEVELOPMENT = os.environ.get("DEVELOPMENT")
    PORT = os.environ.get("PORT")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("POSTGRES_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
