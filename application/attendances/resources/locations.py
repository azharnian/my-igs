from application import db
from application.project.utils import log_activity
from application.attendances.models import Location

@log_activity
def create_location(location_data):
    pass

@log_activity
def get_all_locations():
    pass

@log_activity
def get_location_by_id():
    pass

@log_activity
def update_location(location_id, new_location_data):
    pass

@log_activity
def remove_location(location_id):
    pass

@log_activity
def disable_location(location_id):
    pass