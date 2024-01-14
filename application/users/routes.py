from flask import Blueprint, render_template
from flask_login import login_required

from application.users.forms import *
from application.users.resources import *

users = Blueprint('users', __name__)
