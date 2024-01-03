from flask import Blueprint, render_template

from application.project.utils import log_activity
from application.users.forms import UserLoginForm

admins = Blueprint('admins', __name__)

@admins.route('/', methods=['GET', 'POST'])
@log_activity
def index():
    form = UserLoginForm()
    if form.validate_on_submit():
        pass
 
    return render_template('pages/admins/login.html', form=form)


@admins.route('/dashboard', methods=['GET', 'POST'])
@log_activity
def dashboard():

    title = "Dashboard"
    return render_template('pages/admins/dashboard.html', title=title)

@admins.route('/logout', methods=['GET'])
@log_activity
def logout():
    return 'OK'