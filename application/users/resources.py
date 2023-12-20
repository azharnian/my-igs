from application import db
from application.users.models import *

def create_user(user_data):
    new_user = User(**user_data)
    db.session.add(new_user)
    db.session.commit()
    return "User account has been created successfully"

def get_all_users():
    return User.query.all()

def get_user_by_username(user_username):
    return User.query.filter_by(username=user_username).first()

def get_user_by_email(user_email):
    return User.query.filter_by(email=user_email).first()

def update_user(user_id, new_user_data):
    user_to_update = User.query.get(user_id)

    if user_to_update:
        for key, value in new_user_data.items():
            setattr(new_user_data, key, value)
        db.session.commit()
        return "User account has been updated updated successfully"

    return "User not found"

def remove_user(user_id):
    user_to_remove = User.query.get(user_id)

    if user_to_remove:
        db.session.delete(user_to_remove)
        db.session.commit()

        return "User account has been removed successfully"

    return "User not found"

def suspend_user(user_id):
    user_to_disable = User.query.get(user_id)

    if user_to_disable:
        user_to_disable.is_active = False
        db.session.commit()

        return "User account has been suspended successfully"

    return "User not found"