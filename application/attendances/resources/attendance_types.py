from application import db
from application.project.utils import log_activity
from application.attendances.models import AttendanceType

@log_activity
def create_attendance_type(attendance_type_data):
    pass

@log_activity
def get_all_attendance_types():
    pass

@log_activity
def get_attendance_type_by_id():
    pass

@log_activity
def update_attendance_type(attendance_type_id, new_attendance_type_data):
    pass

@log_activity
def remove_attendance_type(attendance_type_id):
    pass

@log_activity
def disable_attendance_type(attendance_type_id):
    pass