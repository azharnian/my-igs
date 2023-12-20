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
    is_active = db.Column(db.Boolean, nullable = False, default = True)
    is_superuser = db.Column(db.Boolean, nullable = False, default = False)
    is_admin = db.Column(db.Boolean, nullable = False, default = False)
    is_staff = db.Column(db.Boolean, nullable = False, default = False)
    is_student = db.Column(db.Boolean, nullable = False, default = False)

    #Relation with Attendance
    user_attendance = db.relationship('Attendance', backref='user_attendance', lazy=True)
    attendance_input = db.relationship('Attendance', backref='attendance_input', lazy=True)

    #Relation with AttendanceType
    attendancetype_input = db.relationship('AttendanceType', backref='attendancetype_input', lazy=True)

    #Relation with Location
    location_input = db.relationship('Location', backref='location_input', lazy=True)

    #Relation with Status
    status_input = db.relationship('Status', backref='status_input', lazy=True)

    #Relation with Shift
    shift_input = db.relationship('Shift', backref='shift_input', lazy=True)

    #Relation with ShiftMember
    user_shift = db.relationship('ShiftMember', backref='user_shift', lazy=True)
    shift_input = db.relationship('ShiftMember', backref='shift_input', lazy=True)

    #Relation with Achievement
    user_achievement = db.relationship('Achievement', backref='user_achievement', lazy=True)
    achievement_input = db.relationship('Achievement', backref='achievement_input', lazy=True)

    #Relation with Certificate
    user_certificate = db.relationship('Certificate', backref='user_certificate', lazy=True)

    def __repr__(self):
        return f"{self.id} - {self.username} - {self.fullname}"