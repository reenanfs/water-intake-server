from flask_bcrypt import Bcrypt
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    set_access_cookies,
    set_refresh_cookies,
)

from src.user.user_service import UserService
from src.user.user_model import User
from src.common.exceptions.custom_exceptions import (
    UnauthorizedException,
    ConflictException,
    NotFoundException,
    BadRequestException,
)

bcrypt = Bcrypt()


class AuthService:
    @staticmethod
    def login(email: str, password: str) -> tuple[str, str, User]:
        user = UserService.get_by_email(email)
        print("====================================")
        # print(user)
        print("got here")
        if not user or not bcrypt.check_password_hash(user.password, password):
            raise UnauthorizedException("Invalid email or password.")

        access_token, refresh_token = AuthService._generate_tokens(user.id)

        AuthService._update_user_refresh_token(user.id, refresh_token)

        return access_token, refresh_token, user

    @staticmethod
    def register(
        username: str, email: str, password: str
    ) -> tuple[str, str, User]:
        existing_user = UserService.get_by_email(email)

        if existing_user:
            raise ConflictException(msg="Email already in use.")

        hashed_password = bcrypt.generate_password_hash(password).decode(
            "utf-8"
        )

        user_params = {
            "email": email,
            "password": hashed_password,
            "username": username,
        }

        new_user = UserService.create_user(user_params)

        access_token, refresh_token = AuthService._generate_tokens(new_user.id)

        AuthService._update_user_refresh_token(new_user.id, refresh_token)

        return access_token, refresh_token, new_user

    @staticmethod
    def logout(user_id: int):
        UserService.update_user(
            user_id=user_id, user_data={"refresh_token": None}
        )

    @staticmethod
    def profile(user_id: int) -> User:
        user = UserService.get_by_id(user_id)

        if not user:
            raise NotFoundException("User not found")

        return user

    @staticmethod
    def refresh(user_id: int, refresh_token: str) -> tuple[str, str]:
        user = UserService.get_by_id(user_id)

        if not user.refresh_token:
            raise BadRequestException("User has no stored token.")

        if not bcrypt.check_password_hash(user.refresh_token, refresh_token):
            raise UnauthorizedException("Invalid refresh token")

        access_token, refresh_token = AuthService._generate_tokens(user.id)

        AuthService._update_user_refresh_token(
            user_id=user_id, refresh_token=refresh_token
        )

        return access_token, refresh_token

    @staticmethod
    def store_tokens_in_cookies(
        response: dict, access_token: str, refresh_token: str
    ) -> dict:
        set_access_cookies(response, access_token)
        set_refresh_cookies(response, refresh_token)

        return response

    @staticmethod
    def _generate_tokens(user_id: int) -> tuple[str, str]:
        access_token = create_access_token(identity=user_id)
        refresh_token = create_refresh_token(identity=user_id)

        return access_token, refresh_token

    @staticmethod
    def _store_tokens_in_cookies(
        response: dict, access_token: str, refresh_token: str
    ) -> dict:
        set_access_cookies(response, access_token)
        set_refresh_cookies(response, refresh_token)

        return response

    @staticmethod
    def _update_user_refresh_token(user_id: int, refresh_token: str):
        hashed_refresh_token = bcrypt.generate_password_hash(
            refresh_token
        ).decode("utf-8")
        UserService.update_user(
            user_id, {"refresh_token": hashed_refresh_token}
        )
