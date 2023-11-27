from application import db
from application.project.utils import log_activity
from application.grades.models import *

@log_activity
def create_grade_type(grade_type_data):
    pass

@log_activity
def get_all_grade_types():
    pass

@log_activity
def get_grade_type_by_id():
    pass

@log_activity
def update_grade_type(grade_type_id, new_grade_type_data):
    pass

@log_activity
def remove_grade_type(grade_type_id):
    pass

@log_activity
def disable_grade_type(grade_type_id):
    pass