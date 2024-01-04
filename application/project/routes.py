from flask import Blueprint, render_template

from application.project.utils import log_activity
from application.users.forms import UserLoginForm

projects = Blueprint('projects', __name__)

@projects.route('/', methods=['GET', 'POST'])
@log_activity
def index():
    form = UserLoginForm()
    if form.validate_on_submit():
        pass
 
    title = "Login"
    return render_template('login.html', title=title, form=form)


@projects.route('/dashboard', methods=['GET', 'POST'])
@log_activity
def dashboard():

    title = "Dashboard"
    return render_template('pages/users/dashboard.html', title=title)

@projects.route('/about')
@log_activity
def about():
    return render_template('about.html')