from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required

from application.project.utils import log_activity, admin_required

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

from application.admins.users import routes as users_routes
from application.admins.achievements import routes as achievement_routes
from application.admins.certificates import routes as remove_certificate_route