from commons.keys import STATUS, CODE, DATA, MESSAGE
from commons.utils import get_error


class Response:
    def __init__(self, message, status_code, data=None):
        self.message = message
        self.status_code = status_code
        self.data = data

    def to_dict(self):
        response = dict(
            status=dict(
                code=self.status_code,
                message=self.message
            ),
        )

        if self.data is not None:
            response['data'] = self.data
        return response

    def make_response(self):
        return self.to_dict(), self.status_code

    @staticmethod
    def handle_response(result):
        status, message = result[STATUS][CODE], result[STATUS][MESSAGE]
        if status == 200 or 201 or 204:
            return result[DATA]
        return get_error(status, message)


