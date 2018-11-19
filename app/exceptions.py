from werkzeug.exceptions import HTTPException


class DefaultException(HTTPException):

    def __init__(self, description, code=None, message=None):
        self.description = description
        self.code = code
        self.message = message

    def __str__(self):
        return self.description


class InvalidRequest(DefaultException):
    def __init__(self, description, code=400, message=None):
        DefaultException.__init__(self, description=description, code=code, message=message)


class InvalidUsage(DefaultException):
    def __init__(self, description, code=400, message=None):
        DefaultException.__init__(self, description=description, code=code, message=message)


class RequestError(DefaultException):
    def __init__(self, description='', code=500, message=None):
        DefaultException.__init__(self, description=description, code=code, message=message)
