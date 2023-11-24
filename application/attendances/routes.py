from flask import Blueprint, render_template
from flask_login import login_required

from application.attendances.forms.locations import *
from application.attendances.forms.shifts import *
from application.attendances.forms.shift_members import *
from application.attendances.forms.status import *
from application.attendances.forms.attendances import *
from application.attendances.forms.attendance_types import *

from application.attendances.resources.locations import *
from application.attendances.resources.shifts import *
from application.attendances.resources.shift_members import *
from application.attendances.resources.status import *
from application.attendances.resources.attendances import *
from application.attendances.resources.attendance_types import *

attendances = Blueprint('attendances', __name__)

@attendances.route('/attendances/upload')
@login_required
def add_attendances():
    return render_template('pages/attendances/upload_attendances.html')