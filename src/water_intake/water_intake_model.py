from sqlalchemy_serializer import SerializerMixin
from src.database.db import db


class WaterIntake(db.Model, SerializerMixin):
    __tablename__ = "water_intake"

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.TIMESTAMP, default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def __init__(self, user_id: int, amount: float):
        self.user_id = user_id
        self.amount = amount

    def __repr__(self):
        return f"{self.to_dict()}"
