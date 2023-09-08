""" Esto centraliza todos los blueprints
permite habilitar las abreviaciones del código para tenerlo en una sola línea
habilta atajos

"""
from .api import api_scope
from .user import user_scope
from .errors import errors_scope
from .routes import global_scope