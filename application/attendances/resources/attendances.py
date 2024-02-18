import logging

from application import db
from application.project.utils import log_activity
from application.attendances.models import Attendance

@log_activity
def create_attendance(attendance_data):
    try:
        attendance = Attendance(
            created_by = attendance_data['created_by'],
            user_id = attendance_data['user_id'],
            status_id = attendance_data['status_id'],
            type_id = attendance_data['type_id'],
            location_id = attendance_data['location_id'],
            ip_address = attendance_data['ip_address'],
            machine_code = attendance_data['machine_code'],
            image = attendance_data['image'],
            note = attendance_data['note']
        )
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    
    attendance.save()
    return {'success' : True}

@log_activity
def get_all_attendances():
    try:
        ress = Attendance.query.all()
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    
    return ress

@log_activity
def get_attendance_by_id(attendance_id):
    try:
        res = Attendance.query.get(int(attendance_id))
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e

    return res

@log_activity
def update_attendance(attendance_id, new_attendance_data):
    try:
        attendance = Attendance.query.get(int(attendance_id))
        attendance['created_by'] = new_attendance_data['created_by']
        attendance['user_id'] = new_attendance_data['user_id']
        attendance['status_id'] = new_attendance_data['status_id']
        attendance['type_id'] = new_attendance_data['type_id']
        attendance['location_id'] = new_attendance_data['location_id']
        attendance['ip_address'] = new_attendance_data['ip_address']
        attendance['machine_code'] = new_attendance_data['machine_code']
        attendance['image'] = new_attendance_data['image']
        attendance['note'] = new_attendance_data['note']
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    attendance.update()
    return {'success' : True}

@log_activity
def remove_attendance(attendance_id):
    try:
        attendance = Attendance.query.get(int(attendance_id))
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    attendance.remove()
    return {'success' : True}

@log_activity
def disable_attendance(attendance_id):
    try:
        attendance = Attendance.query.get(int(attendance_id))
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    attendance.is_active = False
    attendance.update()
    return {'success' : True}