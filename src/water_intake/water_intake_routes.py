from flask import Blueprint
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
)

from src.water_intake.water_intake_service import WaterIntakeService

water_intake_bp = Blueprint(
    "water_intake", __name__, url_prefix="/waterintake"
)


@water_intake_bp.route("/get-water-intakes", methods=["GET"])
@jwt_required()
def get_water_intake():
    user_id = get_jwt_identity()

    return WaterIntakeService.get_water_intakes(user_id=user_id), 200
