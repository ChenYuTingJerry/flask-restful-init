from flask import Blueprint, jsonify, current_app
from werkzeug.exceptions import HTTPException

from exceptions import DefaultException
from entities.response import ErrorResponse

bp = Blueprint('errors', __name__)


@bp.app_errorhandler(Exception)
@bp.app_errorhandler(HTTPException)
@bp.app_errorhandler(DefaultException)
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
