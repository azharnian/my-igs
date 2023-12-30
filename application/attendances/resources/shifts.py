import logging

from application import db
from application.project.utils import log_activity
from application.attendances.models import Shift

@log_activity
def create_shift(shift_data):
    try:
        shift = Shift(
            is_active = shift_data['is_active'],
            created_by = shift_data['created_by'],
            code = shift_data['code'],
            name = shift_data['name'],
            start_time = shift_data['start_time'],
            end_time = shift_data['end_time']
        )
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    
    shift.save()
    return {'success' : True}

@log_activity
def get_all_shifts():
    try:
        ress = Shift.query.all()
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    
    return ress

@log_activity
def get_shift_by_id(shift_id):
    try:
        res = Shift.query.get(int(shift_id))
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e

    return res

@log_activity
def update_shift(shift_id, new_shift_data):
    try:
        shift = Shift.query.get(int(shift_id))
        shift['is_active'] = new_shift_data['is_active']
        shift['code'] = new_shift_data['code']
        shift['name'] = new_shift_data['name']
        shift['start_time'] = new_shift_data['start_time']
        shift['end_time'] = new_shift_data['end_time']
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    shift.update()
    return {'success' : True}

@log_activity
def remove_shift(shift_id):
    try:
        shift = Shift.query.get(int(shift_id))
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    shift.remove()
    return {'success' : True}

@log_activity
def disable_shift(shift_id):
    try:
        shift = Shift.query.get(int(shift_id))
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    shift.is_active = False
    shift.update()
    return {'success' : True}