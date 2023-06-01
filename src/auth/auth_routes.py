from flask import Blueprint, request
from flask_bcrypt import Bcrypt
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
)

from src.auth.auth_service import AuthService

bcrypt = Bcrypt()
auth_bp = Blueprint("auth", __name__, url_prefix="auth")


@auth_bp.route("/login", methods=["POST"])
def login():
    login_data = request.get_json()

    return AuthService.login(**login_data)


@auth_bp.route("/register", methods=["POST"])
def register():
    register_data = request.get_json()

    return AuthService.register(**register_data)


@auth_bp.route("/logout", methods=["POST"])
@jwt_required
def logout():
    user_id = get_jwt_identity()
    return AuthService.logout(user_id)


@auth_bp.route("/profile", methods=["GET"])
@jwt_required
def profile():
    user_id = get_jwt_identity()
    return AuthService.profile(user_id)


@auth_bp.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    user_id = get_jwt_identity()
    refresh_token = request.cookies.get("refresh_token")

    return AuthService.profile(user_id, refresh_token)
