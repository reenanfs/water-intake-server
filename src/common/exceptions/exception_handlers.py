from src.common.response_handler import ResponseHandler
from jsonschema import ValidationError


def bad_request(error):
    if isinstance(error.description, ValidationError):
        # handle other "flask_expects_json"-errors
        return (
            ResponseHandler.send_error(
                msg=str(error.description.message),
            ),
            404,
        )

    return ResponseHandler.send_error(str(error)), 400


def server_exception(error):
    return (
        ResponseHandler.send_error(
            msg=str(error),
        ),
        500,
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
