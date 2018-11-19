from functools import wraps
from werkzeug.exceptions import BadRequest

from app.exceptions import InvalidRequest


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
            if hasattr(e, 'data'):
                if 'message' in e.data:
                    raise InvalidRequest(description='request parameters, queries or body format are invalid.',
                                         code=e.code, message=e.data.get('message'))
                else:
                    raise InvalidRequest(description=e.description, code=e.code)
            else:
                raise InvalidRequest(e.description, e.code)

    return wrapper
