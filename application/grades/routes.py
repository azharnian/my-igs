from flask import Blueprint, render_template
from flask_login import login_required

from application.grades.forms.subjects import *
from application.grades.forms.grade_types import *
from application.grades.forms.grades import *

from application.grades.resources.subjects import *
from application.grades.resources.grade_types import *
from application.grades.resources.grades import *

grades = Blueprint('grades', __name__)

@grades.route('/grades/upload')
@login_required
def add_grades():
    return render_template('pages/grades/upload_grades.html')