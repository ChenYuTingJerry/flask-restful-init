from flask import Flask
from flasgger import Swagger

from app.api import users, messages, contracts


def register_blueprints(app):
    app.register_blueprint(users.bp, url_prefix='/users')
    app.register_blueprint(messages.bp, url_prefix='/messages')
    app.register_blueprint(contracts.bp, url_prefix='/contracts')


def create_app(config_name='config.config'):
    """

      :param config_name:
      :return:
      """
    app = Flask(__name__)
    app.config.from_object(config_name)
    Swagger(app, template=app.config['SWAGGER_TEMPLATE'])

    # bind db
    with app.app_context():
        from app import errors, logger, request_events
        logger.init(app)
        request_events.init(app)
        errors.init(app)
        # register blueprints
        register_blueprints(app)

        from .signal_handlers import connect_handlers
        connect_handlers()

        from .db import mysql, mongodb
        # init db
        mysql_db = mysql
        mysql_db.init(app)
        mongo_db = mongodb
        mongo_db.init(app)

        # init queue
        from app.msg_queue import producer
        producer.init(app)

    return app
