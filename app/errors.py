from flask import jsonify
from werkzeug.exceptions import HTTPException

from app.entities.response import ErrorResponse
import traceback

def init(app):
    @app.errorhandler(HTTPException)
    def handle_http_exception(error):
        """
                Handle  exception
                :param sender:
                :param error:
                :return:
                """
        status_code = error.code
        response = ErrorResponse(error)
        return jsonify(response), status_code

    @app.errorhandler(Exception)
    def handle_unexpected_exception(error):
        """
                Handle  exception
                :param sender:
                :param error:
                :return:
                """
        traceback.print_exc()
        status_code = 500
        response = ErrorResponse(error)
        return jsonify(response), status_code
