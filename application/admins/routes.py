from flask import Blueprint, render_template, flash, redirect, url_for, abort
from flask_login import login_required, current_user, logout_user, login_user

from werkzeug.security import check_password_hash

from application.project.utils import log_activity, admin_required
from application.users.forms import UserLoginForm, AddUserForm, UpdateUserForm, SearchUserForm
from application.users.resources import create_user, get_user_by_username


from application.certificates.forms import AddCertificateForm, UpdateCertificateForm, AddRevisionForm
from application.certificates.resources import create_certificate,get_all_certificates,get_certificate_by_id,update_certificate,remove_certificate,disable_certificate


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

# CERTIFICATE
@admins.route('/search/certificate', methods=['GET', 'POST'])
@log_activity
@login_required
@admin_required
def search_certificates():
    title = 'Certificate Management'
    certificate = get_all_certificates()
    return render_template('pages/admins/manage_certificates/search_certificates.html', title=title, certificate=certificate)

@admins.route('/add/certificate', methods=['GET', 'POST'])
@log_activity
@login_required
@admin_required
def add_certificate():
    form = AddCertificateForm()

    if form.validate_on_submit():
        res = create_certificate(form.data)
        if res['success']:
            flash(f"Certificate '{form.name.data}' added successfully.", "success")
            return redirect(url_for('admins.search_certificates'))
        else:
            flash("Failed to add certificate.", "danger")

    title = 'Add new certificate'
    return render_template('pages/admins/manage_certificates/add_certificate.html', title=title, form=form)

@admins.route('/update/certificate/<int:certificate_id>', methods=['GET', 'POST'])
@log_activity
@login_required
@admin_required
def update_certificate_route(certificate_id):
    certificate = get_certificate_by_id(certificate_id)  

    if not certificate:
        flash("Certificate not found.", "danger")
        return redirect(url_for('admins.search_certificates'))

    form = UpdateCertificateForm()

    if form.validate_on_submit():
        res = update_certificate(certificate_id, form.data)
        if res['success']:
            flash(f"Certificate '{form.name.data}' updated successfully.", "success")
            return redirect(url_for('admins.search_certificates'))
        else:
            flash("Failed to update certificate.", "danger")

    form.process(obj=certificate)
    title = 'Update certificate'
    return render_template('pages/admins/manage_certificates/update_certificate.html', title=title, form=form)

@admins.route('/remove/certificate/<int:certificate_id>', methods=['GET'])
@log_activity
@login_required
@admin_required
def remove_certificate_route(certificate_id):
    certificate = get_certificate_by_id(certificate_id)

    if not certificate:
        flash("Certificate not found.", "danger")
        return redirect(url_for('admins.search_certificates'))

    res = remove_certificate(certificate_id)
    if res['success']:
        flash("Certificate removed successfully.", "success")
    else:
        flash("Failed to remove certificate.", "danger")

    return redirect(url_for('admins.search_certificates'))

@admins.route('/disable/certificate/<int:certificate_id>', methods=['GET'])
@log_activity
@login_required
@admin_required
def disable_certificate_route(certificate_id):
    certificate = get_certificate_by_id(certificate_id)

    if not certificate:
        flash("Certificate not found.", "danger")
        return redirect(url_for('admins.search_certificates'))

    res = disable_certificate(certificate_id)
    if res['success']:
        flash("Certificate disabled successfully.", "success")
    else:
        flash("Failed to disable certificate.", "danger")

    return redirect(url_for('admins.search_certificates'))