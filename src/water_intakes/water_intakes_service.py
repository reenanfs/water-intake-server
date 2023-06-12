import os
from datetime import datetime

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
    def get_water_intakes(
        user_id: int, start_date: str = None, end_date: str = None
    ) -> list[WaterIntake]:
        user = UsersService.get_by_id(user_id)

        if not user:
            raise BadRequestException("User does not exist.")

        query = WaterIntake.query.filter_by(user_id=user_id)

        if start_date:
            start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
            start_date = datetime.combine(start_date, datetime.min.time())
            query = query.filter(WaterIntake.created_at > start_date)

        if end_date:
            end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
            end_date = datetime.combine(end_date, datetime.max.time())
            query = query.filter(WaterIntake.created_at <= end_date)

        water_intakes = query.all()

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
