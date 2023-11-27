from application import db
from application.project.utils import log_activity
from application.attendances.models import ShiftMember

@log_activity
def create_shift_member(shift_member_data):
    pass

@log_activity
def get_all_shift_members():
    pass

@log_activity
def get_shift_member_by_id():
    pass

@log_activity
def update_shift_member(shift_member_id, new_shift_member_data):
    pass

@log_activity
def remove_shift_member(shift_member_id):
    pass

@log_activity
def disable_shift_member(shift_member_id):
    pass