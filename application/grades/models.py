from application import db
from application.project.models import BaseModel

class GradeType(db.Model, BaseModel):

    __tablename__ = 'grade_types'
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return f''


class Subject(db.Model, BaseModel):

    __tablename__ = 'subjects'
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return f''


class Grade(db.Model, BaseModel):

    __tablename__ = 'grades'
    id = db.Column(db.Integer, primary_key=True)


    def __repr__(self):
        return f''
    