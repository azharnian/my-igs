from datetime import datetime

from flask_login import UserMixin

from application import db
from application.project.models import BaseModel

class User(db.Model, UserMixin, BaseModel):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True, nullable = False)
    password = db.Column(db.String(128), nullable = False)
    first_name = db.Column(db.String(64), nullable = False)
    last_name = db.Column(db.String(64), nullable = False)
    fullname = first_name + last_name
    email = db.Column(db.String(128), unique=True, nullable = False)
    phone = db.Column(db.String(16), unique=True, nullable = False)
    date_joined = db.Column(db.DateTime, nullable = False, default = datetime.utcnow())
    last_ip = db.Column(db.String(15), nullable = False, default = "127.0.0.1")
    last_login = db.Column(db.DateTime, nullable = False, default = datetime.utcnow())
    is_superuser = db.Column(db.Boolean, nullable = False, default = False)
    is_active = db.Column(db.Boolean, nullable = False, default = False)
    is_admin = db.Column(db.Boolean, nullable = False, default = False)
    is_staff = db.Column(db.Boolean, nullable = False, default = False)
    is_student = db.Column(db.Boolean, nullable = False, default = False)



    def __repr__(self):
        return f"{self.id} - {self.username} - {self.fullname}"