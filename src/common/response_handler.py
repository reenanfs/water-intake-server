from flask import make_response
from src.auth.auth_service import AuthService
from flask_jwt_extended import (
    unset_jwt_cookies,
)


class ResponseHandler:
    @staticmethod
    def send_success(data=None, msg=None):
        response = {
            "ok": True,
            "data": data,
            "msg": msg,
        }
        return make_response(response)

    @staticmethod
    def send_set_cookies_success(
        access_token: str,
        refresh_token: str,
        data=None,
        msg=None,
    ):
        response = {
            "ok": True,
            "data": data,
            "msg": msg,
        }

        make_response(response)

        response_with_cookies = AuthService.store_tokens_in_cookies(
            access_token=access_token, refresh_token=refresh_token
        )

        return response_with_cookies

    @staticmethod
    def send_unset_cookies_success(
        data=None,
        msg=None,
    ):
        response = {
            "ok": True,
            "data": data,
            "msg": msg,
        }

        make_response(response)

        unset_jwt_cookies(response)

        return response

    @staticmethod
    def send_error(data: dict | list[dict] = None, msg: str = None):
        response = {
            "ok": False,
            "data": data,
            "msg": msg,
        }
        return make_response(response)
