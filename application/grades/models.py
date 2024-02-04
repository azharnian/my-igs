from application import db
from application.project.models import BaseModel
from datetime import datetime

class GradeType(db.Model, BaseModel):

    __tablename__ = 'grade_types'
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return f''


class Subject(db.Model, BaseModel):

    __tablename__ = 'subjects'
    id = db.Column(db.Integer, primary_key=True)
    subject_taken = db.Column(db.String(32), nullable=False)
    student_id    = db.Column(db.Integer, db.ForeignKey("students.id"), nullable=False)
    assigned_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    description   = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return f'{self.id} - {self.subject_taken}'


class Grade(db.Model, BaseModel):

    __tablename__ = 'grades'
    id = db.Column(db.Integer, primary_key=True)


    def __repr__(self):
        return f''
    