from flask import render_template, flash, redirect, url_for
from flask_login import login_required

from application.admins.routes import admins
from application.project.utils import log_activity, admin_required

from application.certificates.forms import AddCertificateForm, UpdateCertificateForm, AddRevisionForm
from application.certificates.resources import create_certificate,get_all_certificates,get_certificate_by_id,update_certificate,remove_certificate,disable_certificate

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
  