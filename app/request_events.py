import time

from .db import mysql, mongodb
from flask import request, g, current_app as app


def init_app(app):
    @app.before_request
    def before_each_request():
        # record request time
        g.request_start_time = time.time()
        g.request_time = lambda: "%.5fs" % (time.time() - g.request_start_time)

    @app.before_first_request
    def before_first_request():
        pass

    @app.after_request
    def after_each_request(response):
        if not response.status_code % 200 < 100:
            app.logger.debug('db rollback')
            mysql.rollback()
        else:
            app.logger.debug('db commit')
            mysql.commit()

        app.logger.info('"{} {}" request time: {}'.format(request.method, request.path, g.request_time()))

        return response

    @app.teardown_request
    def teardown_each_request(exception=None):
        pass

    @app.teardown_appcontext
    def shutdown(res_or_exc):
        pass
