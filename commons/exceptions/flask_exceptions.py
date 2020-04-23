from flask_api.status import *
from flask_restplus import abort


class ServerError:
    def __init__(self, message):
        abort(HTTP_500_INTERNAL_SERVER_ERROR, status={"code": HTTP_500_INTERNAL_SERVER_ERROR, "message": message})


class BadRequest:
    def __init__(self, message):
        abort(HTTP_400_BAD_REQUEST, status={"code": HTTP_400_BAD_REQUEST, "message": message})


class NotFoundError:
    def __init__(self, message):
        abort(HTTP_404_NOT_FOUND, status={"code": HTTP_404_NOT_FOUND, "message": message})


class MethodNotAllowed:
    def __init__(self, message):
        abort(HTTP_405_METHOD_NOT_ALLOWED, status={"code": HTTP_405_METHOD_NOT_ALLOWED, "message": message})


class UnsupportedMediaTypeError:
    def __init__(self, message):
        abort(HTTP_415_UNSUPPORTED_MEDIA_TYPE, status={"code": HTTP_415_UNSUPPORTED_MEDIA_TYPE, "message": message})


class ResourceAlreadyExistsError:
    def __init__(self, message):
        abort(HTTP_409_CONFLICT, status={"code": HTTP_409_CONFLICT, "message": message})
