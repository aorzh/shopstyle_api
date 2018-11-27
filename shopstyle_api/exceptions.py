class ApiKeyNotFound(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, 'Api key not found', *args, **kwargs)

