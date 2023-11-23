from datetime import datetime

from application import db
from application.project.models import BaseModel

class Log(db.Model, BaseModel):

    __tablename__ = 'logs'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    level = db.Column(db.String(20))
    message = db.Column(db.String(255))