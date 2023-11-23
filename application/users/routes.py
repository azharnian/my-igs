from flask import Blueprint, render_template
from flask_login import login_required

from application.users.forms import *
from application.users.resources import *

users = Blueprint('users', __name__)

@users.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('pages/users/login.html')

@users.route('/account')
@login_required
def account():
    return render_template('pages/users/account.html')