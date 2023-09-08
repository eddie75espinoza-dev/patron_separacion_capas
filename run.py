from sigue import app
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

with app.app_context():
    db.init_app(app)

if __name__ == '__main__':
    app.run(host='localhost', port=5320)