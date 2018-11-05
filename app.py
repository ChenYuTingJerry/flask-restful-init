from flask import Flask, abort
from config import dev, prod, default
from controller import user, test
from exception import common_errors


def configure_app(_app, env):
    """
    Set up a configuration
    :param _app: current application
    :param env: type of the current environment
    :return:
    """
    if env == 'production':
        _app.config.from_object(prod)
    elif env == 'development':
        _app.config.from_object(dev)
    else:
        _app.config.from_object(default)


app = Flask(__name__)
configure_app(app, app.env)

# Registers common errors
app.register_blueprint(common_errors.errors)

# Register blueprints on the application at a URL prefix and/or sub-domain
app.register_blueprint(user.bp, url_prefix='/users')
app.register_blueprint(test.bp, url_prefix='/test')

if __name__ == '__main__':
    app.run(host=app.config.get('HOST'), port=app.config.get('PORT'))
