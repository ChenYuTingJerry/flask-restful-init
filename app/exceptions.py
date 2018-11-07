class DefaultException(Exception):

    def __init__(self, message, status_code=None, data=None):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code
        self.data = data

    def __str__(self):
        return self.message


class InvalidUsage(DefaultException):

    def __init__(self, message, status_code=400, data=None):
        DefaultException.__init__(self, message, status_code, data)


class InvalidRequest(DefaultException):
    def __init__(self, message, status_code=400, data=None):
        DefaultException.__init__(self, message, status_code, data)
