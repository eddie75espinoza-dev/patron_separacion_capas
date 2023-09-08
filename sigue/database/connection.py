""" Este nivel de abstracción permitiría majenar las conexiones en un solo lugar
Acá debe ejecutarse el cursor y las peticiones a la DB
"""
from config import Config

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)

Session = sessionmaker(bind=engine)

Base = declarative_base()

