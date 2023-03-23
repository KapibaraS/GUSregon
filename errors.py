class REGONAPIError(RuntimeError):
    def __init__(self, message, code=None, full_error_obj=None):
        super().__init__(self, message, code, full_error_obj)
        self.message = message
        self.code = code

    def __str__(self):
        return "<REGONAPIError [{}] {}>".format(self.code, self.message)

    __repr__ = __str__
