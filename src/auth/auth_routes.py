from flask_expects_json import expects_json
from flask import Blueprint, request
from flask_bcrypt import Bcrypt
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
)

from src.common.response_handler import ResponseHandler
from src.auth.auth_service import AuthService
from src.auth.auth_validators import login_schema, register_schema


bcrypt = Bcrypt()
auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/register", methods=["POST"])
@expects_json(register_schema, check_formats=True)
def register():
    register_data = request.json
    print("===========================================")
    access_token, refresh_token, new_user = AuthService.register(
        **register_data
    )

    return (
        ResponseHandler.send_set_cookies_success(
            access_token=access_token,
            refresh_token=refresh_token,
            msg="User created successfully.",
            data={"user": new_user.to_dict()},
        ),
        201,
    )


@auth_bp.route("/login", methods=["POST"])
@expects_json(login_schema)
def login():
    login_data = request.json

    access_token, refresh_token, user = AuthService.login(**login_data)
    return (
        ResponseHandler.send_set_cookies_success(
            access_token=access_token,
            refresh_token=refresh_token,
            msg="Login successful",
            data=user.to_dict(),
        ),
        200,
    )


@auth_bp.route("/logout", methods=["POST"])
@jwt_required()
def logout():
    user_id = get_jwt_identity()

    AuthService.logout(user_id)

    return (
        ResponseHandler.send_unset_cookies_success(
            msg="Successfully logged out"
        ),
        200,
    )


@auth_bp.route("/profile", methods=["GET"])
@jwt_required()
def profile():
    user_id = get_jwt_identity()

    user = AuthService.profile(user_id)

    return (
        ResponseHandler.send_success(
            msg="User successfully fetched", data=user.to_dict()
        ),
        200,
    )


@auth_bp.route("/refresh", endpoint="refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    user_id = get_jwt_identity()
    refresh_token = request.cookies.get("refresh_token_cookie")

    access_token, refresh_token = AuthService.refresh(user_id, refresh_token)

    return (
        ResponseHandler.send_set_cookies_success(
            access_token=access_token,
            refresh_token=refresh_token,
            msg="Token refreshed",
        ),
        200,
    )
