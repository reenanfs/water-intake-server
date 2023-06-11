import os
from src.water_intake.water_intake_model import WaterIntake
from src.database.db import db
from src.common.constants.activity_levels import (
    ActivityLevels,
    ACTIVITY_LEVELS,
)


class WaterIntakeService:
    @staticmethod
    def get_water_intakes(user_id: str) -> list[WaterIntake]:
        return WaterIntake.query.filter_by(user_id=user_id).all()

    @staticmethod
    def add_water_intake(user_id: str, amount: float) -> WaterIntake:
        water_intake = WaterIntake(user_id=user_id, amount=amount)
        db.session.add(water_intake)
        db.session.commit()
        return water_intake

    @staticmethod
    def calculate_water_intake(
        weight: float, activity_level: ActivityLevels
    ) -> float:
        target_intake_amount = (
            weight
            * os.environ.get("BASE_INTAKE")
            * ACTIVITY_LEVELS[activity_level]
        )
        return target_intake_amount
