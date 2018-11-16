from flask import jsonify
from werkzeug.exceptions import HTTPException

from app.exceptions import DefaultException
from entities.response import ErrorResponse


def init_app(app):
    @app.errorhandler(DefaultException)
    @app.errorhandler(HTTPException)
    @app.errorhandler(Exception)
    def handle_exception(error):
        """
                Handle  exception
                :param sender:
                :param error:
                :return:
                """
        if isinstance(error, HTTPException):
            status_code = error.code
        else:
            status_code = 500
        response = ErrorResponse(error)
        return jsonify(response.to_dict()), status_code
