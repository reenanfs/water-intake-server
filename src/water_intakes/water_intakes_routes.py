from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_expects_json import expects_json

from src.water_intakes.water_intakes_service import WaterIntakesService
from src.water_intakes.water_intakes_validators import (
    add_water_intake_schema,
    calculate_target_schema,
)
from src.common.response_handler import ResponseHandler


water_intakes_bp = Blueprint(
    "water_intakes", __name__, url_prefix="/water-intakes"
)


@water_intakes_bp.route("/", methods=["GET"])
@jwt_required()
def get_water_intake():
    user_id = get_jwt_identity()
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")

    water_intakes = WaterIntakesService.get_water_intakes(
        user_id=user_id, start_date=start_date, end_date=end_date
    )

    serialized_water_intakes = [
        water_intake.to_dict() for water_intake in water_intakes
    ]

    return (
        ResponseHandler.send_success(
            data=serialized_water_intakes,
            msg="Water Intakes sucessfully retrieved.",
        ),
        200,
    )


@water_intakes_bp.route("/", methods=["POST"])
@jwt_required()
@expects_json(add_water_intake_schema)
def add_water_intake():
    user_id = get_jwt_identity()
    amount = request.json["amount"]

    water_intake = WaterIntakesService.add_water_intake(
        user_id=user_id, amount=amount
    )

    return (
        ResponseHandler.send_success(
            data=water_intake.to_dict(),
            msg="Water intake successfully added.",
        ),
        201,
    )


@water_intakes_bp.route("/calculate-target", methods=["POST"])
@jwt_required()
@expects_json(calculate_target_schema)
def calculate_target():
    request_data = request.json

    target_intake_amount = WaterIntakesService.calculate_target(**request_data)

    return (
        ResponseHandler.send_success(
            data={"target_intake_amount": target_intake_amount},
            msg="Target intake successfully calculated.",
        ),
        200,
    )
