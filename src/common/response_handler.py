class ResponseHandler:
    def send_success(self, data=None, msg=None):
        response = {
            "ok": True,
            "data": data,
            "msg": msg,
        }
        return response

    def send_error(self, data=None, msg=None):
        response = {
            "ok": True,
            "data": data,
            "msg": msg,
        }
        return response
