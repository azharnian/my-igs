from flask_login import UserMixin

from application import db
from application.project.models import BaseModel

class Role(db.Model, BaseModel):

    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)

class User(db.Model, UserMixin, BaseModel):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), nullable = False)
    password = db.Column(db.String(128), nullable = False)
    first_name = db.Column(db.String(64), nullable = False)
    last_name = db.Column(db.String(64), nullable = False)
    email = db.Column(db.String(128), nullable = False)
    phone = db.Column(db.Integer, nullable = False)
    date_joined = db.Column(db.DateTime, nullable = False)
    last_ip = db.Column(db.String(15), nullable = False)
    last_login = db.Column(db.Boolean(), nullable = False)
    is_superuser = db.Column(db.Boolean(), nullable = False)
    is_active = db.Column(db.Boolean(), nullable = False)
    is_admin = db.Column(db.Boolean(), nullable = False)
    is_staff = db.Column(db.Boolean(), nullable = False)
    is_student = db.Column(db.Boolean(), nullable = False)

    def __repr__(self):
        return f"{self.id} - {self.username} - {self.first_name} {self.last_name}"
    