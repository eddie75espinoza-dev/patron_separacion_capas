""" 
Forma alternativa de iniciar la aplicación, esto se puede omitir

para usar con: python3 -m app
"""

from . import app

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


if __name__ == '__main__':
    app.run()