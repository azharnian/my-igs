from application import db
from application.achievements.models import *

def create_achievement(achievement_data):
    new_achievement = Achievement(**achievement_data)
    db.session.add(new_achievement)
    db.session.commit()
    return "Achievement created successfully"

def get_all_achievements():
    return Achievement.query.all()

def get_achievement_by_id(achievement_id):
    return Achievement.query.get(achievement_id)

def update_achievement(achievement_id, new_achievement_data):
    achievement_to_update = Achievement.query.get(achievement_id)

    if achievement_to_update:
        for key, value in new_achievement_data.items():
            setattr(achievement_to_update, key, value)

        db.session.commit()

        return "Achievement updated successfully"

    return "Achievement not found"

def remove_achievement(achievement_id):
    achievement_to_remove = Achievement.query.get(achievement_id)

    if achievement_to_remove:
        db.session.delete(achievement_to_remove)
        db.session.commit()

        return "Achievement removed successfully"

    return "Achievement not found"

def disable_achievement(achievement_id):
    achievement_to_disable = Achievement.query.get(achievement_id)

    if achievement_to_disable:
        achievement_to_disable.status = False
        db.session.commit()

        return "Achievement disabled successfully"

    return "Achievement not found"