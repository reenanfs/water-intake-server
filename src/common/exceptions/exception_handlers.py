from src.common.response_handler import ResponseHandler
from jsonschema import ValidationError


def bad_request_exception(error):
    if hasattr(error, "description") and isinstance(
        error.description, ValidationError
    ):
        if "password" in error.description.path:
            return (
                ResponseHandler.send_error(
                    msg="Invalid email or password",
                ),
                400,
            )
        return (
            ResponseHandler.send_error(
                msg=str(error.description.message),
            ),
            400,
        )
    print(error)
    return ResponseHandler.send_error(str(error)), 400


def server_exception(error: Exception):
    print(error)
    return (
        ResponseHandler.send_error(
            msg=str(error),
        ),
        500,
    )


def not_found_exception(error):
    return (
        ResponseHandler.send_error(
            msg=str(error),
        ),
        404,
    )


def unauthorized_exception(error):
    return (
        ResponseHandler.send_error(
            msg=str(error),
        ),
        401,
    )


def conflict_exception(error):
    return (
        ResponseHandler.send_error(
            msg=str(error),
        ),
        409,
    )
