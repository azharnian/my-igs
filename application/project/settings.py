import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    #secret key
    SECRET_KEY = os.environ.get('SECRET_KEY')
    #sql
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
    #redis
    # REDIS_URL = os.environ.get('REDIS_URL')