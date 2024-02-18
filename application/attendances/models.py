from datetime import datetime

from application import db
from application.project.models import BaseModel
# from application.users.models import User

# Location, Shift, ShiftMember, Status, AttendanceType, Attendance

class Location(db.Model, BaseModel):

    __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column(db.Boolean, nullable=False, default=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), default=1)
    code = db.Column(db.String(256), unique=True, nullable=False)
    name = db.Column(db.String(256), nullable=False)
    longitude = db.Column(db.Float, default=0.0)
    latitude = db.Column(db.Float, default=0.0)
    note = db.Column(db.Text)

    attendances = db.relationship("Attendance", backref = "attendances_in_location", lazy = True)

    def __repr__(self):
        return f'{self.id} - {self.code} - {self.name}'

class Shift(db.Model, BaseModel):

    __tablename__ = 'shifts'
    id = db.Column(db.Integer, primary_key=True)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), default=1)
    code = db.Column(db.String(256), unique=True, nullable=False)
    name = db.Column(db.String(256), nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    note = db.Column(db.Text)

    members = db.relationship("ShiftMember", backref = "members", lazy = True)

    def __repr__(self):
        return f'{self.id} - {self.code} - {self.name}'

class ShiftMember(db.Model, BaseModel):

    __tablename__ = 'shift_members'
    id = db.Column(db.Integer, primary_key=True)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    date_joined = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), default=1)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    shift_id = db.Column(db.Integer, db.ForeignKey('shifts.id'), nullable=False)

    def __repr__(self):
        return f'{self.id} - {self.user_id} - {self.shift_id}'

class Status(db.Model, BaseModel): #masuk , izin, sakit, dispensasi

    __tablename__ = 'status'
    id = db.Column(db.Integer, primary_key=True)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), default=1)
    code = db.Column(db.String(10), unique=True, nullable=False)
    name = db.Column(db.String(256), nullable=False)
    note = db.Column(db.Text)

    attendances = db.relationship("Attendance", backref = "attendances_in_status", lazy = True)

    def __repr__(self):
        return f'{self.id} - {self.code} - {self.name}'

class AttendanceType(db.Model, BaseModel):

    __tablename__ = 'attendance_types'
    id = db.Column(db.Integer, primary_key=True)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), default=1)
    name = db.Column(db.String(256), nullable=False)
    note = db.Column(db.Text)

    attendances = db.relationship("Attendance", backref = "attendances_in_type", lazy = True)

    def __repr__(self):
        return f'{self.id} - {self.name}'

class Attendance(db.Model, BaseModel):

    __tablename__ = 'attendances'
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column(db.Boolean, nullable=False, default=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, default=1)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    status_id = db.Column(db.Integer, db.ForeignKey('status.id'), nullable=False, default=1)
    type_id = db.Column(db.Integer, db.ForeignKey('attendance_types.id'), nullable=False, default=1)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=False, default=1)
    ip_address = db.Column(db.String(64), nullable=False, default='127.0.0.1')
    machine_code = db.Column(db.String(256), nullable=False, default='0X')
    image = db.Column(db.String(256))
    note = db.Column(db.Text)



    def __repr__(self):
        return f'{self.id} - {self.user_id} - {self.status_id} - {self.location_id}'
    