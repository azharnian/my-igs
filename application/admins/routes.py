from flask import Blueprint, render_template, flash, redirect, url_for, abort
from flask_login import login_required, current_user, logout_user, login_user

from werkzeug.security import check_password_hash

from application.project.utils import log_activity, admin_required
from application.users.forms import UserLoginForm, AddUserForm, UpdateUserForm, SearchUserForm
from application.users.resources import create_user, get_user_by_username

from application.achievements.forms import AddAchievementForm, UpdateAchievementForm, AddRevisionForm
from application.achievements.resources import create_achievement,get_all_achievements,get_achievement_by_id,update_achievement,remove_achievement,disable_achievement


admins = Blueprint('admins', __name__)


@admins.route('/', methods=['GET', 'POST'])
@log_activity
@login_required
@admin_required
def index():

    title = "Dashboard"
    return render_template('pages/admins/dashboard.html', title=title)


@admins.route('/logout', methods=['GET'])
@log_activity
@login_required
@admin_required
def logout():
    return redirect(url_for('projects.logout'))

#USERS
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


# ACHIEVEMENTS
@admins.route('/search/achievements', methods=['GET', 'POST'])
@log_activity
@login_required
@admin_required
def search_achievements():
    title = 'Achievement Management'
    achievements = get_all_achievements()
    return render_template('pages/admins/manage_achievements/search_achievements.html', title=title, achievements=achievements)

@admins.route('/add/achievement', methods=['GET', 'POST'])
@log_activity
@login_required
@admin_required
def add_achievement():
    form = AddAchievementForm()

    if form.validate_on_submit():
        res = create_achievement(form.data)
        if res['success']:
            flash(f"Achievement '{form.name.data}' added successfully.", "success")
            return redirect(url_for('admins.search_achievements'))
        else:
            flash("Failed to add achievement.", "danger")

    title = 'Add new achievement'
    return render_template('pages/admins/manage_achievements/add_achievement.html', title=title, form=form)

@admins.route('/update/achievement/<int:achievement_id>', methods=['GET', 'POST'])
@log_activity
@login_required
@admin_required
def update_achievement_route(achievement_id):
    achievement = get_achievement_by_id(achievement_id)  

    if not achievement:
        flash("Achievement not found.", "danger")
        return redirect(url_for('admins.search_achievements'))

    form = UpdateAchievementForm()

    if form.validate_on_submit():
        res = update_achievement(achievement_id, form.data)
        if res['success']:
            flash(f"Achievement '{form.name.data}' updated successfully.", "success")
            return redirect(url_for('admins.search_achievements'))
        else:
            flash("Failed to update achievement.", "danger")

    form.process(obj=achievement)
    title = 'Update achievement'
    return render_template('pages/admins/manage_achievements/update_achievement.html', title=title, form=form)

@admins.route('/remove/achievement/<int:achievement_id>', methods=['GET'])
@log_activity
@login_required
@admin_required
def remove_achievement_route(achievement_id):
    achievement = get_achievement_by_id(achievement_id)

    if not achievement:
        flash("Achievement not found.", "danger")
        return redirect(url_for('admins.search_achievements'))

    res = remove_achievement(achievement_id)
    if res['success']:
        flash("Achievement removed successfully.", "success")
    else:
        flash("Failed to remove achievement.", "danger")

    return redirect(url_for('admins.search_achievements'))

@admins.route('/disable/achievement/<int:achievement_id>', methods=['GET'])
@log_activity
@login_required
@admin_required
def disable_achievement_route(achievement_id):
    achievement = get_achievement_by_id(achievement_id)

    if not achievement:
        flash("Achievement not found.", "danger")
        return redirect(url_for('admins.search_achievements'))

    res = disable_achievement(achievement_id)
    if res['success']:
        flash("Achievement disabled successfully.", "success")
    else:
        flash("Failed to disable achievement.", "danger")

    return redirect(url_for('admins.search_achievements'))