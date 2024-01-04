from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required

from application.project.utils import log_activity, admin_required
from application.users.forms import UserLoginForm, AddUserForm, UpdateUserForm, SearchUserForm
from application.users.resources import create_user

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

#USERS
@admins.route('/search/user', methods=['GET', 'POST'])
@log_activity
# @login_required
# @admin_required
def search_user():
    form = SearchUserForm()

    title = 'User Management'
    return render_template('pages/admins/manage_user/search_user.html', title=title, form=form)

@admins.route('/add/user', methods=['GET', 'POST'])
@log_activity
def add_user():
    form = AddUserForm()
    
    if form.validate_on_submit():
        res = create_user(form.data)
        if res['success']:
            flash(f"{form.username.data} account created.", "success")
            return redirect(url_for('admins.search_user'))

    title = 'Add new user'
    return render_template('pages/admins/manage_user/add_user.html', title=title, form=form)

@admins.route('/update/user', methods=['GET', 'POST'])
@log_activity
def update_user():
    form = UpdateUserForm()

    title = 'Update user'
    return render_template('pages/admins/manage_user/update_user.html', title=title, form=form)
