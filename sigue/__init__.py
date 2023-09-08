""" Instanciación de la aplicación"""


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_jwt_extended import JWTManager

from config import Config
from .routes import global_scope, api_scope, errors_scope, user_scope


app = Flask(__name__, static_folder=Config.STATIC_FOLDER, template_folder=Config.TEMPLATE_FOLDER)
app.config.from_object(Config)
# jwt = JWTManager(app)

db = SQLAlchemy(app)

# Registrar las vistas
app.register_blueprint(global_scope, url_prefix='/')
app.register_blueprint(errors_scope, url_prefix='/sigue/v1')
app.register_blueprint(user_scope, url_prefix='/sigue/v1/user')
app.register_blueprint(api_scope, url_prefix='/sigue/v1/application')
