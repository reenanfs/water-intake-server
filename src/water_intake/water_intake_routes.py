from flask import Blueprint, request
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
)
from flask_expects_json import expects_json

from src.water_intake.water_intake_service import WaterIntakeService
from src.water_intake.water_intake_validators import (
    add_water_intake_schema,
    get_target_intake_amount_schema,
)
from src.common.response_handler import ResponseHandler


water_intake_bp = Blueprint(
    "water_intake", __name__, url_prefix="/waterintake"
)


@water_intake_bp.route("/get-water-intakes", methods=["GET"])
@jwt_required()
def get_water_intake():
    user_id = get_jwt_identity()
    water_intakes = WaterIntakeService.get_water_intakes(user_id=user_id)
    return (
        ResponseHandler.send_success(
            data=water_intakes, msg="Water Intakes sucessfully retrieved."
        ),
        200,
    )


@water_intake_bp.route("/add-water-intake", methods=["POST"])
@jwt_required()
@expects_json(add_water_intake_schema)
def add_water_intake():
    user_id = get_jwt_identity()
    amount = request.json["amount"]
    water_intake = WaterIntakeService.add_water_intake(
        user_id=user_id, amount=amount
    )
    return (
        ResponseHandler.send_success(
            data=water_intake, msg="Water Intakes sucessfully retrieved."
        ),
        201,
    )


@water_intake_bp.route("/get-target_intake_amount", methods=["GET"])
@jwt_required()
@expects_json(get_target_intake_amount_schema)
def get_target_intake_amount():
    request_data = request.json
    target_intake_amount = WaterIntakeService(**request_data)

    return (
        ResponseHandler.send_success(
            data={"target_intake_amount": target_intake_amount},
            msg="Target intake successfully calculated.",
        ),
        200,
    )
