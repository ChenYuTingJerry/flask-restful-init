class DefaultException(Exception):

    def __init__(self, message, code=None, data=None):
        Exception.__init__(self)
        self.message = message
        self.code = code
        self.data = data

    def __str__(self):
        return self.message


class InvalidUsage(DefaultException):

    def __init__(self, message, code=400, data=None):
        DefaultException.__init__(self, message, code, data)


class InvalidRequest(DefaultException):
    def __init__(self, message, code=400, data=None):
        DefaultException.__init__(self, message, code, data)
