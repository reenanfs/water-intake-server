import os

from src.water_intakes.water_intakes_model import WaterIntake
from src.database.db import db
from src.users.users_service import UsersService
from src.common.constants.activity_levels import (
    ActivityLevels,
)
from src.common.exceptions.custom_exceptions import (
    BadRequestException,
)


class WaterIntakesService:
    @staticmethod
    def get_water_intakes(user_id: int) -> list[WaterIntake]:
        user = UsersService.get_by_id(user_id)

        if not user:
            raise BadRequestException("User does not exist.")

        water_intakes = WaterIntake.query.filter_by(user_id=user_id).all()
        print("======", water_intakes)

        return water_intakes

    @staticmethod
    def add_water_intake(user_id: int, amount: float) -> WaterIntake:
        user = UsersService.get_by_id(user_id)

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
