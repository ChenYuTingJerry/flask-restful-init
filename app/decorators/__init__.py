from functools import wraps
from werkzeug.exceptions import BadRequest

from app.entities.exceptions import InvalidRequest


def valid_request(func):
    """
    Check  request is valid.
    :param func:
    :return:
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except BadRequest as e:
            raise InvalidRequest(description='request parameters, queries or body format are invalid.',
                                 code=e.code, message=e.data.get('message'))

    return wrapper
