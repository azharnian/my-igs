from flask import render_template, redirect, url_for, flash
from flask_login import login_required

from application.admins.routes import admins
from application.project.utils import log_activity, admin_required

from application.users.forms import SearchUserForm, AddUserForm, UpdateUserForm
from application.users.resources import create_user



@admins.route('/search/user', methods=['GET', 'POST'])
@log_activity
@login_required
@admin_required
def search_user():
    form = SearchUserForm()

    title = 'User Management'
    return render_template('pages/admins/manage_user/search_user.html', title=title, form=form)

@admins.route('/add/user', methods=['GET', 'POST'])
@log_activity
@login_required
@admin_required
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
@login_required
@admin_required
def update_user():
    form = UpdateUserForm()

    title = 'Update user'
    return render_template('pages/admins/manage_user/update_user.html', title=title, form=form)
