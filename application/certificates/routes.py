from flask import Blueprint, render_template
from flask_login import login_required

from application.certificates.forms import *
from application.certificates.resources import *

certificates = Blueprint('certificates', __name__)

@certificates.route('/certificate/add')
@login_required
def add_certificate():
    return render_template('pages/certificates/add_certificate.html')