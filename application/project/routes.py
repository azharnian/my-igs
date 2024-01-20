from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user

from werkzeug.security import check_password_hash

from application.project.utils import log_activity, student_required
from application.users.forms import UserLoginForm
from application.users.resources import get_user_by_username

projects = Blueprint('projects', __name__)

@projects.route('/', methods=['GET', 'POST'])
@log_activity
def index():
    if current_user.is_authenticated:
        return redirect(url_for('projects.dashboard'))
    form = UserLoginForm()
    if form.validate_on_submit():
        user = get_user_by_username(form.username.data)

        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('projects.dashboard'))
        flash('Something went wrong, please check your username and password again.', 'danger')
 
    title = "Login"
    return render_template('login.html', title=title, form=form)


@projects.route('/dashboard', methods=['GET', 'POST'])
@log_activity
@login_required
@student_required
def dashboard():
    
    title = "Dashboard"
    return render_template('pages/users/dashboard.html', title=title)

@projects.route('/logout')
@log_activity
@login_required
def logout():
    logout_user()
    return redirect(url_for('projects.index'))

@projects.route('/about')
@log_activity
def about():
    return render_template('about.html')