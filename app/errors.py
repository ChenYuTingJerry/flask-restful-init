from flask import Blueprint, jsonify
from werkzeug.exceptions import HTTPException

from app.exceptions import DefaultException
from entities.response import ErrorResponse
import traceback
import sys
import logging

log = logging.getLogger('errors')
bp = Blueprint('errors', __name__)


@bp.app_errorhandler(DefaultException)
def handle_exception(error):
    """
    Handle custom exception inherit DefaultException
    :param error:
    :return:
    """
    status_code = error.code
    response = ErrorResponse(error)
    return jsonify(response.to_dict()), status_code


@bp.app_errorhandler(HTTPException)
def handle_http_except_error(error):
    """
    Handle all HTTP exception
    :param error: HTTPException
    :return:
    """
    status_code = error.code
    response = ErrorResponse(error)
    return jsonify(response.to_dict()), status_code


@bp.app_errorhandler(Exception)
def handle_unknown_exception(error):
    traceback.print_exc(file=sys.stdout)
    status_code = 500
    response = ErrorResponse(error)
    return jsonify(response.to_dict()), status_code
