from logging import FileHandler
import logging


def init(app):
    log_handler = FileHandler(app.config['LOG_PATH'])
    formatter = logging.Formatter(app.config['LOG_FORMAT'])
    log_handler.setFormatter(formatter)

    # set the app logger level
    app.logger.setLevel(app.config['LOG_LEVEL'])

    app.logger.addHandler(log_handler)

