import sys


class _Const:
    class ConstError(TypeError):
        pass

    class ConstCaseError(TypeError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__.keys():
            raise self.ConstError("Can't change const.%s" % name)
        if not name.isupper():
            raise self.ConstCaseError('const name %r is not all uppercase' % name)
        self.__dict__[name] = value

    def __init__(self):
        self.JSON = 'application/json'
        self.MPEG = 'video/mpeg'
        self.JPEG = 'image/jpeg'
        self.HTML = 'text/html'
        self.PDF = 'application/pdf'
        self.URL_ENCODED = 'application/x-www-form-urlencoded'
        self.TEXT = 'text/plain'
        self.PNG = 'image/png'
        self.OCTET_STREAM = 'application/octet-stream'


sys.modules[__name__] = _Const()
