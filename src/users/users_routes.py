from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from flask_expects_json import expects_json

from src.users.users_service import UsersService
from src.users.users_validators import update_user_schema
from src.common.response_handler import ResponseHandler

users_bp = Blueprint("users", __name__, url_prefix="/users")


@users_bp.route("/<user_id>", methods=["PUT"])
@jwt_required()
@expects_json(update_user_schema)
def update_user(user_id):
    request_data = request.json

    updated_user = UsersService.update_user(user_id, request_data)

    return (
        ResponseHandler.send_success(
            data=updated_user.to_dict(), msg="User successfully updated."
        ),
        200,
    )
