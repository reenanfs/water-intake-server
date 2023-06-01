from src.user.user_model import User
from src.database.db import db


class UserService:
    @staticmethod
    def get_users() -> list[User]:
        users = User.query.all()
        serialized_users = [user.to_dict() for user in users]
        return serialized_users

    @staticmethod
    def get_by_email(email: str) -> User:
        user = User.query.filter_by(email=email).one_or_none()
        if not user:
            return None
        serialized_user = user.to_dict()
        return serialized_user

    @staticmethod
    def get_by_id(id: int) -> User:
        user = User.query.filter_by(id=id).one_or_none()
        if not user:
            return None
        serialized_user = user.to_dict()
        return serialized_user

    @staticmethod
    def create_user(user_data: dict) -> User:
        user = User(**user_data)
        db.session.add(user)
        db.session.commit()

        serialized_user = user.to_dict()
        return serialized_user

    @staticmethod
    def update_user(user: User, user_data: dict) -> User:
        deserialized_user = User(**user)

        for key, value in user_data.items():
            if hasattr(deserialized_user, key):
                setattr(deserialized_user, key, value)

        db.session.commit()

        serialized_user = deserialized_user.to_dict()
        return serialized_user
