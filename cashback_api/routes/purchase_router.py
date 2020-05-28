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

from .schemas.purchase_schema import PurchaseSchema


class PurchaseRouter(Resource):
    def __init__(self):
        self.cashbackService = CashbackService()
        self.purchaseSchema = PurchaseSchema()

    @jwt_required
    @authorize(["manager", "support", "default"])
    def get(self):
        try:
            cpf = get_jwt_identity()
            purchases = self.cashbackService.get_purchases(cpf)
        except Exception as e:
            return error(e)
        else:
            return ok(data=purchases)

    @jwt_required
    @authorize(["manager", "support", "default"])
    def post(self):
        json = request.get_json() or None
        if json is None:
            return bad_request()

        try:
            cpf = get_jwt_identity()
            data = self.purchaseSchema.load(json)
            self.cashbackService.register_purchase(cpf, data)
        except NotUniqueError:
            return bad_request("This sale code is already in use")
        except MongoValidationError as e:
            return bad_request('Error storage', e.message)
        except SchemaValidationError as e:
            return bad_request('Invalid request', e.messages)
        except Exception as e:
            return error(e)
        else:
            return ok(data=f'Sale {json["code"]} saved')
