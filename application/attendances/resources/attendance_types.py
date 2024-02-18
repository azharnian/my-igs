import logging

from application import db
from application.project.utils import log_activity
from application.attendances.models import AttendanceType

@log_activity
def create_attendance_type(attendance_type_data):
    try:
        attendance_type = AttendanceType(
            is_active = attendance_type_data['is_active'],
            created_by = attendance_type_data['created_by'],
            name = attendance_type_data['name']
        )
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    
    attendance_type.save()
    return {'success' : True}

@log_activity
def get_all_attendance_types():
    try:
        ress = AttendanceType.query.all()
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    
    return ress

@log_activity
def get_attendance_type_by_id(attendance_type_id):
    try:
        res = AttendanceType.query.get(int(attendance_type_id))
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e

    return res

@log_activity
def update_attendance_type(attendance_type_id, new_attendance_type_data):
    try:
        attendance_type = AttendanceType.query.get(int(attendance_type_id))
        attendance_type['is_active'] = new_attendance_type_data['is_active']
        attendance_type['user_id'] = new_attendance_type_data['user_id']
        attendance_type['shift_id'] = new_attendance_type_data['shift_id']
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    attendance_type.update()
    return {'success' : True}

@log_activity
def remove_attendance_type(attendance_type_id):
    try:
        attendance_type = AttendanceType.query.get(int(attendance_type_id))
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    attendance_type.remove()
    return {'success' : True}

@log_activity
def disable_attendance_type(attendance_type_id):
    try:
        attendance_type = AttendanceType.query.get(int(attendance_type_id))
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    attendance_type.is_active = False
    attendance_type.update()
    return {'success' : True}