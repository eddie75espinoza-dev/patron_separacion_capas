# entre las capas solo deberían pasarse objetos definidos en os modelos
from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from ..controllers import applications_controllers


user_scope = Blueprint('user', __name__)

# con blueprint usa el url_prefix definido en __init__.py
# equivalente a: /api/applications
@user_scope.get('/<user>')
# @jwt_required()
def user_info(user):

    # current_user = get_jwt_identity()
    current_user = user

    return {
        "username": current_user
    }