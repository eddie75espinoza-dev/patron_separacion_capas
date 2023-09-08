import os
from dotenv import load_dotenv

load_dotenv()


BEARER = os.environ.get('BEARER', '')

USER = os.environ.get('USER')
PASS = os.environ.get('PASS')
HOST = os.environ.get('HOST')
PORT = os.environ.get('PORT')
DB = os.environ.get('DB')
DB_TOKEN = os.environ.get('DB_TOKEN', '')


class Config():
    DEBUG = True
    BEARER = BEARER
    
    DB_TOKEN = DB_TOKEN
    
    SQLALCHEMY_DATABASE_URI = f'postgresql://{USER}:{PASS}@{HOST}:{PORT}/{DB}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    TEMPLATE_FOLDER = 'views/templates/'
    STATIC_FOLDER = 'views/static/'