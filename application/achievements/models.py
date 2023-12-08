from application import db
from application.project.models import BaseModel
from datetime import datetime
from application.users.models import User 

class AchievementType(db.Model, BaseModel):

    __tablename__ = "achievement_types"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category = db.Column(db.String(64), nullable=False)
    level = db.Column(db.String(64), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    status = db.Column(db.Boolean, default=True)
    online = db.Column(db.Boolean, default=False)

    achievements = db.relationship('AchievementType', backref='achievements_in type')

class Achievement(db.Model, BaseModel):

    __tablename__ = 'achievements'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    organizer = db.Column(db.String(128), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('achievement_types.id'), nullable=False)
    input_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    description = db.Column(db.String(256))
    comp_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) #tanggal lomba
    start_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    end_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


    def __repr__(self):
        return f'Achievement(id={self.id}, achievement={self.achievement}, organizer={self.organizer}, student={self.student}, type={self.achievement_type}, input_by={self.input_user})'