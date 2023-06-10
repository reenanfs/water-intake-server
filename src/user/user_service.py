from src.user.user_model import User
from src.database.db import db
from src.common.exceptions.custom_exceptions import (
    NotFoundException,
)


class UserService:
    @staticmethod
    def get_users() -> list[User]:
        return User.query.all()

    @staticmethod
    def get_by_email(email: str) -> User:
        return User.query.filter_by(email=email).one_or_none()

    @staticmethod
    def get_by_id(id: int) -> User:
        return User.query.filter_by(id=id).one_or_none()

    @staticmethod
    def create_user(user_data: dict) -> User:
        user = User(**user_data)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def update_user(user_id: int, user_data: dict) -> User:
        user = UserService.get_by_id(user_id)

        if not user:
            raise NotFoundException("User not found")

        allowed_props = [prop.key for prop in User.__table__.columns]
        invalid_props = set(user_data.keys()) - set(allowed_props)
        if invalid_props:
            raise ValueError(f'Invalid properties: {", ".join(invalid_props)}')

        for prop, value in user_data.items():
            setattr(user, prop, value)

        db.session.commit()

        return user
