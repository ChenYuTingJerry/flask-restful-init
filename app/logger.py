import logging
from logging.handlers import RotatingFileHandler


def init_app(app):
    log_handler = RotatingFileHandler('./log/app.log', maxBytes=1000, backupCount=1)

    # set the log handler level
    log_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('[%(asctime)-12s] %(levelname)s in %(module)s %(message)s')
    log_handler.setFormatter(formatter)
    # set the app logger level
    app.logger.setLevel(logging.INFO)

    app.logger.addHandler(log_handler)
