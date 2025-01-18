from falcon import HTTPError
import falcon.status_codes as status


class Forbidden(HTTPError):
    def __init__(self):
        description = "Access forbidden"
        super().__init__(status.HTTP_403, description=description)


class InsufficientData(HTTPError):
    def __init__(self, msg=None):
        description = msg or "Insufficient Data"
        super().__init__(status.HTTP_400, description=description)


class UnauthorizedError(HTTPError):
    def __init__(self):
        description = "Operation Not Authorized"
        super().__init__(status.HTTP_403, description=description)


class InvalidArgumentError(HTTPError):
    def __init__(self):
        description = "Invalid argument"
        super().__init__(status.HTTP_400, description=description)
