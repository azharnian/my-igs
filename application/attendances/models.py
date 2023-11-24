from application import db
from application.project.models import BaseModel

class AttendanceType(db.Model, BaseModel):

    __tablename__ = "attendance_types"
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return f''


class Attendance(db.Model, BaseModel):

    __tablename__ = 'attendances'
    id = db.Column(db.Integer, primary_key=True)


    def __repr__(self):
        return f''
    