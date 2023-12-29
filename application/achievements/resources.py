from application import db
import logging
from application.project.utils import log_activity
from application.achievements.models import *

@log_activity
def create_achievement(achievement_data):
    try:
        achievement = Achievement(
            created_by = achievement_data['created_by'],
            organizer = achievement_data['organizer'],
            descripton =  achievement_data['descripton'],
            comp_date = achievement_data['comp_date'],
            start_date = achievement_data['start_date'],
            end_date = achievement_data['end_date']
        )
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    
    achievement.save()
    return {'success' : True}

@log_activity
def get_all_achievements():
    try:
        ress = Achievement.query.all()
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    return ress

@log_activity
def get_achievement_by_id(achievement_id):
    try:
        res = Achievement.query.get(int(achievement_id))
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e

    return res

@log_activity    
def update_achievement(achievement_id, new_achievement_data):
    try:
        achievement = Achievement.query.get(int(achievement_id))
        achievement['created_by'] = new_achievement_data['created_by']
        achievement['organizer'] =  new_achievement_data['organizer']
        achievement['descripton'] = new_achievement_data['description']
        achievement['comp_date'] =  new_achievement_data['comp_date']
        achievement['start_date'] = new_achievement_data['start_date']
        achievement['end_date'] = new_achievement_data['end_date']
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    achievement.update()
    return {'success' : True}

@log_activity
def remove_achievement(achievement_id):
    try:
        achievement = Achievement.query.get(int(achievement_id))
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    achievement.remove()    
    return {'success' : True}

@log_activity
def disable_achievement(achievement_id):
    try:
        achievement = Achievement.query.get(int(achievement_id))
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    achievement.is_activate = False
    achievement.update()    
    return {'success' : True}
