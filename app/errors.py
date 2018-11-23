from flask import jsonify
from werkzeug.exceptions import HTTPException

from app.entities.response import ErrorResponse


def init_app(app):
    @app.errorhandler(HTTPException)
    def handle_exception(error):
        """
                Handle  exception
                :param sender:
                :param error:
                :return:
                """
        status_code = error.code
        response = ErrorResponse(error)
        return jsonify(response), status_code
