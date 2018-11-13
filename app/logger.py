from logging.handlers import RotatingFileHandler
import logging

def init_app(app):
    log_handler = RotatingFileHandler(app.config['LOG_PATH'])

    formatter = logging.Formatter('[%(asctime)-12s] %(levelname)s in %(module)s %(message)s')
    log_handler.setFormatter(formatter)
    # set the app logger level
    app.logger.setLevel(app.config['LOG_LEVEL'])

    app.logger.addHandler(log_handler)
