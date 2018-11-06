from lib.entity import Entity


class Response(Entity):
    def __init__(self, status):
        self.status = status


class ErrorResponse(Response):

    def __init__(self, error=None, status=1):
        Response.__init__(self, status)
        if error:
            data = error.data if hasattr(error, 'data') else None
            self.error = ErrorResponse.to_payload(error.__class__.__name__, str(error), data)
        else:
            self.error = {}

    @staticmethod
    def to_payload(error_type, error_msg, error_data):
        payload = dict()
        payload.update({
            'type': error_type,
            'message': error_msg
        })

        if error_data:
            payload['payload'] = error_data

        return payload


class SuccessResponse(Response):
    def __init__(self, data=None, status=0):
        Response.__init__(self, status)
        if data:
            if type(data) is dict:
                self.data = data
            elif isinstance(data, Entity):
                self.data = data.__dict__
        else:
            self.data = {}
