from flask_jwt_extended import JWTManager
from src.common.response_handler import ResponseHandler

jwt = JWTManager()


@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_data):
    return (
        ResponseHandler.send_error(
            msg="The token has expired",
        ),
        401,
    )


@jwt.invalid_token_loader
def invalid_token_callback(error_msg):
    return (
        ResponseHandler.send_error(
            msg=error_msg,
        ),
        422,
    )


@jwt.unauthorized_loader
def unauthorized_callback(error_msg):
    return (
        ResponseHandler.send_error(
            msg=error_msg,
        ),
        401,
    )


@jwt.needs_fresh_token_loader
def needs_fresh_token_callback():
    return (
        ResponseHandler.send_error(
            msg="Fresh token required",
        ),
        401,
    )


@jwt.revoked_token_loader
def revoked_token_callback():
    return (
        ResponseHandler.send_error(
            msg="Token has been revoked",
        ),
        401,
    )
