from flask import request

from flask_restful import Resource
from marshmallow.exceptions import ValidationError as SchemaValidationError
from mongoengine.errors import NotUniqueError
from mongoengine.errors import ValidationError as MongoValidationError
from resources.http_response import bad_request, error, ok
from services.reseller_service import ResellerService

from .schemas.reseller_register_schema import ResellerRegisterSchema


class ResellerRegisterRouter(Resource):
    def __init__(self):
        self.resellerService = ResellerService()
        self.resellerRegisterSchema = ResellerRegisterSchema()

    def post(self, *args, **kwargs):
        json = request.get_json() or None
        if json is None:
            return bad_request('Invalid data')

        try:
            data = self.resellerRegisterSchema.load(json)
            reseller = self.resellerService.create(data, register=True)
        except NotUniqueError:
            return bad_request("This email OR cpf already exist")
        except MongoValidationError as e:
            return bad_request('Error storage', e.message)
        except SchemaValidationError as e:
            return bad_request('Invalid request', e.messages)
        except Exception as e:
            return error(e)
        else:
            return ok(data=reseller)
