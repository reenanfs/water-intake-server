import os

from src.water_intake.water_intake_model import WaterIntake
from src.database.db import db
from src.user.user_service import UserService
from src.common.constants.activity_levels import (
    ActivityLevels,
)
from src.common.exceptions.custom_exceptions import (
    BadRequestException,
)


class WaterIntakeService:
    @staticmethod
    def get_water_intakes(user_id: str) -> list[WaterIntake]:
        user = UserService.get_by_id(user_id)

        if not user:
            raise BadRequestException("User does not exist.")
        print(user_id)
        water_intakes = WaterIntake.query.filter_by(user_id=user_id).all()

        for water_intake in water_intakes:
            print(water_intake)

        print("oi")
        return water_intakes

    @staticmethod
    def add_water_intake(user_id: str, amount: float) -> WaterIntake:
        user = UserService.get_by_id(user_id)

        if not user:
            raise BadRequestException("User does not exist.")

        water_intake = WaterIntake(user_id=user_id, amount=amount)
        db.session.add(water_intake)
        db.session.commit()
        return water_intake

    @staticmethod
    def calculate_target(
        weight: float, activity_level: ActivityLevels
    ) -> float:
        target_intake_amount = (
            weight
            * float(os.environ.get("BASE_INTAKE"))
            * ActivityLevels[activity_level].value
        )
        return target_intake_amount
