from flask import Blueprint, render_template
from flask_login import login_required

from application.achievements.forms import *
from application.achievements.resources import *

achievements = Blueprint('achievements', __name__)

@achievements.route('/achievements/add')
@login_required
def add_achievements():
    return render_template('pages/achievements/add_achievement.html')