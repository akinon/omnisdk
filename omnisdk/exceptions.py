class _WithJsonMixin(Exception):
    def __init__(self, *a, **kw):
        self.json = kw.pop("json")
        super(_WithJsonMixin, self).__init__(*a, **kw)

class ValidationError(_WithJsonMixin):
    pass

class ClientException(Exception):
    pass

class ClientNotInitializedException(ClientException):
    pass

class ClientMissingParameterException(ClientException):
    pass

class ClientBadUrlException(ClientException):
    pass
