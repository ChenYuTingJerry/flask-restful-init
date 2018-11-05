import sys


class __Const:
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
        self.CONTENT_TYPE = 'Content-Type'
        self.AUTHORIZATION = 'Authorization'


sys.modules[__name__] = __Const()

