from application import db
from application.project.utils import log_activity
from application.attendances.models import Status

@log_activity
def create_status(status_data):
    pass

@log_activity
def get_all_status():
    pass

@log_activity
def get_status_by_id():
    pass

@log_activity
def update_status(status_id, new_status_data):
    pass

@log_activity
def remove_status(status_id):
    pass

@log_activity
def disable_status(status_id):
    pass