from flask import Flask
from config import config
from api import user, test
import errors


def create_app(config_name):
    """

      :param config_name:
      :return:
      """
    app = Flask(__name__)

    if type(config_name) is not str:
        app.config.from_object(config['default'])
    else:
        app.config.from_object(config[config_name])

    # register blueprints
    app.register_blueprint(errors.bp)
    app.register_blueprint(user.bp, url_prefix='/users')
    app.register_blueprint(test.bp, url_prefix='/test')

    return app
