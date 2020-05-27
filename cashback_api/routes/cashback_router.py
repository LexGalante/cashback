from flask import request

from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource
from marshmallow.exceptions import ValidationError as SchemaValidationError
from mongoengine.errors import NotUniqueError
from mongoengine.errors import ValidationError as MongoValidationError
from resources.errors import NotFoundError
from resources.http_response import bad_request, error, ok
from resources.jwt import authorize
from services.reseller_service import ResellerService


class CashbackRouter(Resource):
    def __init__(self):
        self.resellerService = ResellerService()

    @jwt_required
    @authorize(["manager", "support", "default"])
    def get(self):
        pass
