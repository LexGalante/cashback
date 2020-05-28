from flask import request

from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource
from marshmallow.exceptions import ValidationError as SchemaValidationError
from mongoengine.errors import NotUniqueError
from mongoengine.errors import ValidationError as MongoValidationError
from resources.errors import NotFoundError
from resources.http_response import bad_request, error, ok
from resources.jwt import authorize
from services.cashback_service import CashbackService


class CashbackRouter(Resource):
    def __init__(self):
        self.cashbackService = CashbackService()

    @jwt_required
    @authorize(["manager", "support", "default"])
    def get(self):
        try:
            cpf = get_jwt_identity()
            cashback = self.cashbackService.calcule_cashback(cpf)
        except Exception as e:
            return error(e)
        else:
            return ok(data=cashback)
