from flask_bcrypt import Bcrypt
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    set_access_cookies,
    set_refresh_cookies,
    unset_jwt_cookies,
)

from src.user.user_service import UserService
from src.user.user_model import User
from src.common.response_handler import ResponseHandler
from src.common.exceptions.custom_exceptions import UnauthorizedException
from src.common.exceptions.custom_exceptions import ConflictException

bcrypt = Bcrypt()


class AuthService:
    @staticmethod
    def login(email: str, password: str):
        user = UserService.get_by_email(email)
        if not user or not bcrypt.check_password_hash(user.password, password):
            raise UnauthorizedException("Invalid email or password.")

        tokens = AuthService._generate_tokens(user.id)

        response = ResponseHandler.send_success(
            msg="Login successful", data=user
        )

        response_with_cookies = AuthService._store_tokens_in_cookies(
            response, tokens
        )

        return response_with_cookies

    @staticmethod
    def register(username: str, email: str, password: str):
        existing_user = UserService.get_by_email(email)

        if existing_user:
            raise ConflictException(
                msg="User with that identifier already exists."
            )

        hashed_password = bcrypt.generate_password_hash(password).decode(
            "utf-8"
        )

        user_params = {
            "email": email,
            "password": hashed_password,
            "username": username,
        }

        new_user = UserService.create_user(user_params)

        tokens = AuthService._generate_tokens(new_user.id)

        AuthService._update_user_refresh_token(new_user, tokens.refresh_token)

        response = ResponseHandler.send_success(
            msg="User created successfully.", data=new_user
        )

        response_with_cookies = AuthService._store_tokens_in_cookies(
            response, tokens
        )

        return response_with_cookies

    @staticmethod
    def logout(user_id: int):
        user = UserService.get_by_id(user_id)

        UserService.update_user(user, {"refresh_token": None})

        response = ResponseHandler.send_success(msg="Successfully logged out")
        unset_jwt_cookies(response)
        return response

    @staticmethod
    def profile(user_id: int):
        user = UserService.get_by_id(user_id)

        if not user:
            return ResponseHandler.send_error(msg="User not found"), 404

        return ResponseHandler.send_success(
            msg="User successfully fetched", data=user
        )

    @staticmethod
    def refresh(user_id: int, refresh_token: str):
        user = UserService.get_by_id(user_id)

        if not bcrypt.check_password_hash(
            refresh_token.encode("utf-8"), user.refresh_token.encode("utf-8")
        ):
            return ResponseHandler.send_error("Invalid refresh token"), 401

        tokens = AuthService._generate_tokens(user.id)

        UserService.update_user(user, {"refresh_token": tokens.refresh_token})

        response = ResponseHandler.send_success(msg="Token refreshed")

        response_with_cookies = AuthService._store_tokens_in_cookies(
            response, tokens
        )

        return response_with_cookies

    def _generate_tokens(self, user_id: int) -> dict[str, str]:
        access_token = create_access_token(sub=user_id)
        refresh_token = create_refresh_token(sub=user_id)

        return {"access_token": access_token, "refresh_token": refresh_token}

    def _store_tokens_in_cookies(
        response: dict, tokens: dict[str, str]
    ) -> dict:
        set_access_cookies(response, tokens.access_token)
        set_refresh_cookies(response, tokens.refresh_token)

        return response

    def _update_user_refresh_token(user: User, refresh_token: str) -> dict:
        hashed_refresh_token = bcrypt.generate_password_hash(
            refresh_token
        ).decode("utf-8")
        UserService.update_user(user, {"refresh_token": hashed_refresh_token})
