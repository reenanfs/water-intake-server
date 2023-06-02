class ResponseHandler:
    @staticmethod
    def send_success(data=None, msg=None):
        response = {
            "ok": True,
            "data": data,
            "msg": msg,
        }
        return response

    @staticmethod
    def send_error(data: dict | list[dict] = None, msg: str = None):
        response = {
            "ok": True,
            "data": data,
            "msg": msg,
        }
        return response
