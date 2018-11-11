from functools import wraps
from werkzeug.exceptions import HTTPException
from app.exceptions import InvalidRequest
from flask import current_app as app


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
        except HTTPException as e:
            if hasattr(e, 'data'):
                if 'message' in e.data:
                    raise InvalidRequest(e.description, e.code, e.data.get('message'))
                else:
                    raise InvalidRequest(e.description, e.code)
            else:
                raise InvalidRequest(e.description, e.code)

    return wrapper

