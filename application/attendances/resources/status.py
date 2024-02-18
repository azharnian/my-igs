import logging

from application import db
from application.project.utils import log_activity
from application.attendances.models import Status

@log_activity
def create_status(status_data):
    try:
        status = Status(
            is_active = status_data['is_active'],
            created_by = status_data['created_by'],
            code = status_data['code'],
            name = status_data['name']
        )
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    
    status.save()
    return {'success' : True}

@log_activity
def get_all_status():
    try:
        ress = Status.query.all()
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    
    return ress

@log_activity
def get_status_by_id(status_id):
    try:
        res = Status.query.get(int(status_id))
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e

    return res
@log_activity
def update_status(status_id, new_status_data):
    try:
        status = Status.query.get(int(status_id))
        status['is_active'] = new_status_data['is_active']
        status['code'] = new_status_data['code']
        status['name'] = new_status_data['name']
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    status.update()
    return {'success' : True}

@log_activity
def remove_status(status_id):
    try:
        status = Status.query.get(int(status_id))
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    status.remove()
    return {'success' : True}

@log_activity
def disable_status(status_id):
    try:
        status = Status.query.get(int(status_id))
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    status.is_active = False
    status.update()
    return {'success' : True}