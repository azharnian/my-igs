import logging

from application import db
from application.project.utils import log_activity
from application.attendances.models import ShiftMember

@log_activity
def create_shift_member(shift_member_data):
    try:
        shift_member = ShiftMember(
            is_active = shift_member_data['is_active'],
            created_by = shift_member_data['created_by'],
            user_id = shift_member_data['user_id'],
            shift_id = shift_member_data['shift_id']
        )
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    
    shift_member.save()
    return {'success' : True}

@log_activity
def get_all_shift_members():
    try:
        ress = ShiftMember.query.all()
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    
    return ress

@log_activity
def get_shift_member_by_id(shift_member_id):
    try:
        res = ShiftMember.query.get(int(shift_member_id))
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e

    return res

@log_activity
def update_shift_member(shift_member_id, new_shift_member_data):
    try:
        shift_member = ShiftMember.query.get(int(shift_member_id))
        shift_member['is_active'] = new_shift_member_data['is_active']
        shift_member['user_id'] = new_shift_member_data['user_id']
        shift_member['shift_id'] = new_shift_member_data['shift_id']
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    shift_member.update()
    return {'success' : True}

@log_activity
def remove_shift_member(shift_member_id):
    try:
        shift_member = ShiftMember.query.get(int(shift_member_id))
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    shift_member.remove()
    return {'success' : True}

@log_activity
def disable_shift_member(shift_member_id):
    try:
        shift_member = ShiftMember.query.get(int(shift_member_id))
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    shift_member.is_active = False
    shift_member.update()
    return {'success' : True}