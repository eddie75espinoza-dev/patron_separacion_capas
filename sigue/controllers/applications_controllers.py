# la capa controller solo debe interactuar con los datos de application
# esto mantiene aislada la capa de lógica de la capa de presentación

from ..database import sigue_db
from ..models.models import Application


def lists():
    return sigue_db.list_all()
