from application import db
from application.project.models import BaseModel
from datetime import datetime


class GradeType(db.Model, BaseModel):
    __tablename__ = 'grade_types'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(32), nullable=False) #nilai pas,nilai to,nilai pts
    assigned_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) #kapan test dikerjakan dan mendapatkan nilai    

    grades = db.relationship("Grade", backref="grade_type", lazy=True)

    def __repr__(self):
        return f'{self.id} - {self.category}'


class Subject(db.Model, BaseModel):

    __tablename__ = 'subjects'
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return f''

class Grade(db.Model, BaseModel):
    __tablename__ = 'grades'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("students.id"), nullable=False)
    grade_type_id = db.Column(db.Integer, db.ForeignKey("grade_types.id"), nullable=False)
    value = db.Column(db.String(10), nullable=False) #nilai yang diperoleh
    description = db.Column(db.String(256), nullable=False)
    date = db.Column(db.DateTime, nullable=False)


    grade_type = db.relationship("GradeType", backref="grades", lazy=True)

    def __repr__(self):
        return f'{self.id} - {self.student} - {self.grade_type} - {self.value}'
