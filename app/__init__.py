from flask import Flask
from .db import get_db
from config import config
from app.api import test_req, users
from app import errors


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

    # bind db
    with app.app_context():
        sql_db = get_db('sql')
        sql_db.init_db(app)

        no_sql_db = get_db('nosql')
        no_sql_db.init_db(app)

    # register blueprints
    app.register_blueprint(errors.bp)
    app.register_blueprint(users.bp, url_prefix='/users')
    app.register_blueprint(test_req.bp, url_prefix='/test')

    return app
