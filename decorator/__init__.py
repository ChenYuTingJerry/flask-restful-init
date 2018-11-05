import json
from functools import wraps

from werkzeug.exceptions import HTTPException

from exception import InvalidRequest


def parse_request(func):
    """
    Hadle flask.
    :param func:
    :return:
    """
    @wraps(func)
    def parse(*args, **kwargs):
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

    return parse
