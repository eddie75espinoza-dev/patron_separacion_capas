from flask import Blueprint, render_template


# Define un alcance de trabajo
global_scope = Blueprint('views', __name__) # Definimos rutas

nav = [{'name': 'all applications', 'url': 'v1/application'}] # nombre y url para la barra de navegación

#@global_scope.route('/', methods=['GET'])
@global_scope.get('/sigue/v1')
def home():
    """ Landing page route"""

    parameters = {'title': 'SIGUE',
                  'description': 'Sistema de Internet Gratuito Unico para Estudiantes'
                  }
    
    return render_template('index.html', nav=nav, **parameters)
