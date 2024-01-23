import logging

from werkzeug.security import generate_password_hash

from application import db
from application.project.utils import log_activity
from application.users.models import *

@log_activity
def create_user(user_data):
    try:
        user = User(
            email = user_data['email'],
            phone = user_data['phone'],
            first_name = user_data['first_name'],
            last_name = user_data['last_name'],
            fullname = user_data['first_name']+ ' ' + user_data['last_name'],
            username = user_data['username'],
            is_student = True,
            password = generate_password_hash(user_data['password'], method='pbkdf2:sha256')
        )
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    
    user.save()
    return {'success' : True}

@log_activity
def get_all_users():
    try:
        ress = User.query.all()
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    
    return ress

@log_activity
def get_user_by_username(user_username):
    try:
        ress = User.query.filter_by(username=user_username).first()
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    
    return ress

@log_activity
def get_user_by_email(user_email):
    try:
        ress = User.query.filter_by(email=user_email).first()
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    
    return ress

@log_activity
def get_user_by_id(user_id):
    try:
        ress = User.query.filter_by(id=user_id).first()
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    
    return ress

@log_activity
def update_user(user_id, new_user_data):
    try:
        user = User.query.get(int(user_id))
        user['username'] = new_user_data['username'],
        user['password'] = new_user_data['new_password']
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    user.update()
    return {'success' : True}

@log_activity
def remove_user(user_id):
    try:
        user = User.query.get(int(user_id))
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    user.remove()
    return {'success' : True}

@log_activity
def suspend_user(user_id):
    try:
        user = User.query.get(int(user_id))
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    user.is_active = False
    user.update()
    return {'success' : True}

@log_activity
def assign_admin(username):
    try:
        user = get_user_by_username(username)
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    user.is_admin = True
    user.update()
    return {'success' : True}