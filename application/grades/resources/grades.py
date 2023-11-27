from application import db
from application.project.utils import log_activity
from application.grades.models import *

@log_activity
def create_grade(grade_data):
    pass

@log_activity
def get_all_grades():
    pass

@log_activity
def get_grade_by_id():
    pass

@log_activity
def update_grade(grade_id, new_grade_data):
    pass

@log_activity
def remove_grade(grade_id):
    pass

@log_activity
def disable_grade(grade_id):
    pass