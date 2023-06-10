class UnauthorizedException(Exception):
    def __init__(self, msg=None):
        super().__init__(msg)
        self.msg = msg


class ConflictException(Exception):
    def __init__(self, msg=None):
        super().__init__(msg)
        self.msg = msg


class NotFoundException(Exception):
    def __init__(self, msg=None):
        super().__init__(msg)
        self.msg = msg


class BadRequestException(Exception):
    def __init__(self, msg=None):
        super().__init__(msg)
        self.msg = msg
