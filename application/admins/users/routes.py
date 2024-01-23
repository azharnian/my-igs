from flask import render_template, flash, redirect, url_for
from flask_login import login_required

from application.admins.routes import admins
from application.project.utils import log_activity, admin_required
from application.users.forms import UserLoginForm, AddUserForm, UpdateUserForm, SearchUserForm, AssignAdminForm
from application.users.resources import create_user, get_all_users, get_user_by_username, get_user_by_id, update_user, remove_user, suspend_user, assign_admin

@admins.route('/remove/user', methods=['GET', 'POST'])
@log_activity
@login_required
@admin_required
def removing_user(user_id):
    user = get_user_by_id(user_id)
    res = remove_user(user_id)
    if res['success']:
        flash(f"{user.username} account removed.", "success")
        return redirect(url_for('admins.search_user'))

    title = 'Remove user'
    return render_template('pages/admins/manage_user/remove_user.html', title=title)

@admins.route('/suspend/user', methods=['GET', 'POST'])
@log_activity
@login_required
@admin_required
def suspending_user(user_id):
    user = get_user_by_id(user_id)
    res = suspend_user(user_id)
    if res['success']:
        flash(f"{user.username} account suspended.", "success")
        return redirect(url_for('admins.search_user'))

    title = 'Suspend user'
    return render_template('pages/admins/manage_user/suspend_user.html', title=title)


@admins.route('/assign/user', methods=['GET', 'POST'])
@log_activity
@login_required
@admin_required
def assign_admin():
    form = AssignAdminForm()

    if form.validate_on_submit():
        res = assign_admin(form.data)
        if res ['success']:
            flash(f"{form.username.data} account assigned as admin.", "success")
            return redirect(url_for('admins.search_user'))
        
    title = "Assign Admin"
    return render_template('pages/admins/manage_user/assign_admin.html', title=title, form=form)

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

#USERS
@admins.route('/search/user', methods=['GET', 'POST'])
@log_activity
@login_required
@admin_required
def search_user(username):
    form = SearchUserForm(username)
    
    if form.validate_on_submit():
        user = get_user_by_username(form.data)
        return user

    title = 'User Management'
    return render_template('pages/admins/manage_user/search_user.html', title=title, form=form)

@admins.route('/view/all_users', methods=['GET', 'POST'])
@log_activity
@login_required
@admin_required
def view_all_users():
    users = get_all_users()

    title = "View All Users"
    return render_template('pages/admins/manage_user/view_all_users.html', title=title, users=users)

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
def updating_user(user_id):
    form = UpdateUserForm()

    if form.validate_on_submit():
        res = update_user(user_id,form.data)
        if res['success']:
            flash(f"{form.username.data} account updated.", "success")
            return redirect(url_for('admins.search_user'))

    title = 'Update user'
    return render_template('pages/admins/manage_user/update_user.html', title=title, form=form)