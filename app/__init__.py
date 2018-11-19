from flask import Flask
from config import config
from app.api import test_req, users, orders


def register_blueprints(app):
    app.register_blueprint(users.bp, url_prefix='/users')
    app.register_blueprint(orders.bp, url_prefix='/orders')
    app.register_blueprint(test_req.bp, url_prefix='/test_req')


def create_app(config_name):
    """

      :param config_name:
      :return:
      """
    app = Flask(__name__)
    if config_name not in config:
        app.config.from_object(config['default'])
    else:
        app.config.from_object(config[config_name])

    # bind db
    with app.app_context():
        from app import errors, logger, request_events
        logger.init_app(app)
        request_events.init_app(app)
        errors.init_app(app)
        # register blueprints
        register_blueprints(app)

        from .signal_handlers import connect_handlers
        connect_handlers()

        from .db import mysql, mongodb
        # init db
        mysql_db = mysql
        mysql_db.init_db(app)
        mongo_db = mongodb
        mongo_db.init_db(app)

    return app
