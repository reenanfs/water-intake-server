from sqlalchemy_serializer import SerializerMixin
from src.database.db import db


class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    weight = db.Column(db.String, nullable=True)
    activity_level = db.Column(db.String, nullable=True)
    refresh_token = db.Column(db.String, nullable=True)
    water_intakes = db.relationship("WaterIntake", backref="user", lazy=True)

    def __init__(
        self,
        username: str,
        email: str,
        password: str,
        refresh_token: str,
        weight: float = None,
        activity_level: str = None,
    ):
        self.username = (username,)
        self.email = (email,)
        self.password = (password,)
        self.refresh_token = (refresh_token,)
        self.weight = (weight,)
        self.activity_level = activity_level

    def __repr__(self):
        return f"{self.to_dict()}"
