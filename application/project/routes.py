from flask import Blueprint, render_template

from application.project.utils import log_activity

projects = Blueprint('projects', __name__)

@projects.route('/')
@log_activity
def index():
    return str(True)

@projects.route('/about')
@log_activity
def about():
    return render_template('about.html')