class OSSLookupError(LookupError):

    def __init__(self, *args, **kwargs):
        LookupError.__init__(self, *args, **kwargs)
