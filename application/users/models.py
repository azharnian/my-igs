from flask_login import UserMixin

from application import db
from application.project.models import BaseModel

class Role(db.Model, BaseModel):

    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)


class User(db.Model, UserMixin, BaseModel):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)


    def __repr__(self):
        return f''
    