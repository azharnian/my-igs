import logging

from application import db
from application.project.utils import log_activity
from application.users.models import *

def create_user(user_data):
    try:
        user = User(
            email = user_data['email'],
            phone = user_data['phone'],
            first_name = user_data['first_name'],
            last_name = user_data['last_name'],
            username = user_data['username'],
            password = user_data['password']
        )
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    
    user.save()
    return {'success' : True}

def get_all_users():
    try:
        ress = User.query.all()
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    
    return ress

def get_user_by_username(user_username):
    try:
        ress = User.query.filter_by(username=user_username).first()
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    
    return ress

def get_user_by_email(user_email):
    try:
        ress = User.query.filter_by(email=user_email).first()
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    
    return ress

def update_user(user_id, new_user_data):
    try:
        user = User.query.get(int(user_id))
        user['username'] = new_user_data['username'],
        user['phone'] = new_user_data['phone']
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    user.update()
    return {'success' : True}

def remove_user(user_id):
    try:
        user = User.query.get(int(user_id))
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    user.remove()
    return {'success' : True}

def suspend_user(user_id):
    try:
        user = User.query.get(int(user_id))
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    user.is_active = False
    user.update()
    return {'success' : True}