from flask import Blueprint, make_response, jsonify, request
from flask_login import login_required

from application.project.utils import log_activity

api = Blueprint('api', __name__)

@api.route('/api')
# @login_required
@log_activity
def api_():
    context = {
        'status' : True,
        'message' : 'api is running'
    }
    return make_response(jsonify(context), 200)