from application import db
from application.project.models import BaseModel

class AchievementType(db.Model, BaseModel):

    __tablename__ = "achievement_types"
    id = db.Column(db.Integer, primary_key=True)


class Achievement(db.Model, BaseModel):

    __tablename__ = 'achievements'
    id = db.Column(db.Integer, primary_key=True)


    def __repr__(self):
        return f''
    