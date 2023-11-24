from application import db
from application.project.utils import log_activity
from application.attendances.models import Shift

@log_activity
def create_shift(shift_data):
    pass

@log_activity
def get_all_shifts():
    pass

@log_activity
def get_shift_by_id():
    pass

@log_activity
def update_shift(shift_id, new_shift_data):
    pass

@log_activity
def remove_shift(shift_id):
    pass

@log_activity
def disable_shift(shift_id):
    pass