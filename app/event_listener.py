from .db import mysql


def init_app(app):
    @app.before_request
    def before_each_request():
        app.logger.debug('before_each_request')

    @app.before_first_request
    def before_first_request():
        app.logger.debug('before_first_request')

    @app.after_request
    def after_each_request(response):
        app.logger.info('after_each_request: {}'.format(response.status_code))
        if not 0 <= (response.status_code - 200) < 100:
            app.logger.info('db rollback')
            mysql.rollback()
        else:
            app.logger.info('db commit')
            mysql.commit()
        return response

    @app.teardown_request
    def teardown_each_request(exception=None):
        pass

    @app.teardown_appcontext
    def shutdown(res_or_exc):
        pass
