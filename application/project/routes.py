from flask import Blueprint, render_template

projects = Blueprint('projects', __name__)

@projects.route('/')
def index():
    return str(True)

@projects.route('/about')
def about():
    return render_template('about.html')