
(
    PREV_OPERATION_CORRECTLY, OUT_DATED_CODE, TOO_MANY_IDENTIFIES,
    NO_ENTITY_FOUND, INVALID_OR_EMPTY, NO_SESSION
) = (0, 1, 2, 4, 5, 7)

mapper_codes = {
    PREV_OPERATION_CORRECTLY: 403,
    OUT_DATED_CODE: 403,
    TOO_MANY_IDENTIFIES: 400,
    NO_ENTITY_FOUND: 400,
    INVALID_OR_EMPTY: 400,
    NO_SESSION: 401,
}


class REGONAPIError(RuntimeError):
    def __init__(self, message, code=None, full_error_obj=None):
        super().__init__(self, message, code, full_error_obj)
        self.message = str(message)

        self.code = mapper_codes.get(code) or code

    def __str__(self):
        return "<REGONAPIError [{}] {}>".format(self.code, self.message)

    __repr__ = __str__
