import logging

from application import db
from application.project.utils import log_activity
from application.attendances.models import Location

@log_activity
def create_location(location_data):
    try:
        location = Location(
            created_by = location_data['created_by'],
            code = location_data['code'],
            name = location_data['name'],
            longitude = location_data['longitude'],
            latitude = location_data['latitude'],
            note = location_data['note']
        )
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    
    location.save()
    return {'success' : True}

@log_activity
def get_all_locations():
    try:
        ress = Location.query.all()
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    
    return ress

@log_activity
def get_location_by_id(location_id):
    try:
        res = Location.query.get(int(location_id))
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e

    return res

@log_activity
def update_location(location_id, new_location_data):
    try:
        location = Location.query.get(int(location_id))
        location['created_by'] = new_location_data['created_by'],
        location['code'] = new_location_data['code'],
        location['name'] = new_location_data['name'],
        location['longitude'] = new_location_data['longitude'],
        location['latitude'] = new_location_data['latitude'],
        location['note'] = new_location_data['note']
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    location.update()
    return {'success' : True}

@log_activity
def remove_location(location_id):
    try:
        location = Location.query.get(int(location_id))
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    location.remove()
    return {'success' : True}


@log_activity
def disable_location(location_id):
    try:
        location = Location.query.get(int(location_id))
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    location.is_active = False
    location.update()
    return {'success' : True}