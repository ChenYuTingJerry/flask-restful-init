from werkzeug.exceptions import HTTPException


class CustomException(HTTPException):

    def __init__(self, description, code=None, message=None):
        self.description = description
        self.code = code
        self.message = message

    def __str__(self):
        return self.description


class InvalidRequest(CustomException):
    def __init__(self, description, code=400, message=None):
        super().__init__(description=description, code=code, message=message)


class InvalidUsage(CustomException):
    def __init__(self, description, code=400, message=None):
        super().__init__(description=description, code=code, message=message)


class RequestError(CustomException):
    def __init__(self, description='', code=500, message=None):
        super().__init__(description=description, code=code, message=message)
