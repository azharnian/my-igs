from functools import wraps
import logging

from flask import redirect, url_for, abort, flash
from flask_login import current_user, logout_user

from application import login_manager
from application.users.models import User
from application.logs.resources import *

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            user = f"{current_user.username} : {current_user.fullname}"
        except:
            user = 'Guest'
        try:
            result = func(*args, **kwargs)
            data = {
                'level':'INFO', 
                'message':f"{func.__name__} executed successfully by {user}"
            }
            create_log(data)
            logging.info(f"{func.__name__} executed successfully by {user}")
            return result
        except Exception as e:
            data = {
                'level':'ERROR', 
                'message':f"An error occurred in {func.__name__}: {str(e)} by {user}"
            }
            create_log(data)
            logging.error(f"An error occurred in {func.__name__}: {str(e)}")
            raise e

    return wrapper

def admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not current_user.is_admin:
            return abort(403)
        return func(*args, **kwargs)

    return wrapper

def student_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not current_user.is_student:
            return redirect(url_for('admins.index'))
        return func(*args, **kwargs)

    return wrapper