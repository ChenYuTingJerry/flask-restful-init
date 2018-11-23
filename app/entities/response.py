from utils.entity import Entity


class Response(Entity):
    def __init__(self, status):
        super().__init__()
        self['status'] = status


class ErrorResponse(Response):

    def __init__(self, error=None, status=1):
        super().__init__(status)
        message = error.message if hasattr(error, 'message') else None
        self['error'] = ErrorResponse.to_payload(error.__class__.__name__, str(error), message) if error else {}

    @staticmethod
    def to_payload(error_type, error_msg, error_data):
        payload = dict()
        payload.update({
            'type': error_type,
            'description': error_msg
        })

        if error_data:
            payload['message'] = error_data

        return payload


class SuccessResponse(Response):
    def __init__(self, data=None, status=0):
        super().__init__(status)
        self['data'] = data if data else {}
