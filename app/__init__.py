from flask import Flask
from config import config
from app.api import test_req, users
from app import errors, logger, event_listener
from .db import mysql, mongodb


def register_blueprints(app):
    app.register_blueprint(errors.bp)
    app.register_blueprint(users.bp, url_prefix='/users')
    app.register_blueprint(test_req.bp, url_prefix='/test_req')


def create_app(config_name):
    """

      :param config_name:
      :return:
      """
    app = Flask(__name__)
    #
    if config_name not in config:
        app.config.from_object(config['default'])
    else:
        app.config.from_object(config[config_name])

    logger.init_app(app)
    event_listener.init_app(app)

    # register blueprints
    register_blueprints(app)

    # bind db
    with app.app_context():
        mysql_db = mysql
        mysql_db.init_db(app)
        mongo_db = mongodb
        mongo_db.init_db(app)

    return app
