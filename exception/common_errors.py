from flask import Blueprint, jsonify
from werkzeug.exceptions import HTTPException

from exception import DefaultException
from entities.response import ErrorResponse

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(Exception)
@errors.app_errorhandler(HTTPException)
@errors.app_errorhandler(DefaultException)
def handle_global_exception(error):
    """
    Handle custom exception inherit DefaultException
    :param error:
    :return:
    """
    if isinstance(error, DefaultException):
        status_code = error.status_code
    else:
        status_code = 500
    response = ErrorResponse(error)
    return jsonify(response.to_dict()), status_code

# @errors.errorhandler(HTTPException)
# def handle_http_except_error(error):
#     """
#     Handle all HTTP exception
#     :param error: HTTPException
#     :return:
#     """
#     print('ffff')
#     status_code = error.code
#     response = HttpErrorResponse(error)
#     return jsonify(response.to_dict()), status_code
