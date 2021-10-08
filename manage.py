from flask_migrate import stamp, upgrade, current
from flask_script import Manager

from sqlalchemy_utils import database_exists

from app.models import db, app, init_db
from config import Config

manager = Manager(app)

@manager.command
def db_create():
    init_db()
    stamp()

@manager.command
def setup():
    if database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
        upgrade()
    else:
        db_create()


if __name__ == '__main__':
    manager.run()
