from application import db
from application.project.utils import log_activity
from application.attendances.models import Attendance

@log_activity
def create_attendance(attendance_data):
    pass

@log_activity
def get_all_attendances():
    pass

@log_activity
def get_attendance_by_id():
    pass

@log_activity
def update_attendance(attendance_id, new_attendance_data):
    pass

@log_activity
def remove_attendance(attendance_id):
    pass

@log_activity
def disable_attendance(attendance_id):
    pass