# entre las capas solo deberían pasarse objetos definidos en los modelos
from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from ..controllers import applications_controllers


api_scope = Blueprint('application', __name__)

# con blueprint usa el url_prefix definido en __init__.py
# equivalente a: /api/applications
@api_scope.get('/')
def get_applications():
    # la capa controlador genera la consulta a la DB
    # applications_list = applications_controllers.lists()
    
    # Como se debe presentar un formato de salida tipo dict, se asigna para devolver la respuesta    
    # applications_dict = [application.asdict() for application in applications_list]

    # conversión a tipo json
    #return jsonify(applications_dict)
    return {'applications': 'all applications'}
