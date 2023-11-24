from flask import Blueprint, render_template
from flask_login import login_required

from application.attendances.forms import *
from application.attendances.resources import *

attendances = Blueprint('attendances', __name__)

@attendances.route('/attendances/upload')
@login_required
def add_attendances():
    return render_template('pages/attendances/upload_attendances.html')