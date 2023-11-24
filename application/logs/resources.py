from application import db
from application.logs.models import *

def create_log(log_data):
    log = Log(level=log_data['level'], message=log_data['message'])
    log.save()

def get_all_logs():
    return Log.query.all()