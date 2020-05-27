from flask import request

from resources.jwt import authorize
from resources.http_response import bad_request, error, ok
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource
from marshmallow.exceptions import ValidationError as SchemaValidationError
from mongoengine.errors import NotUniqueError
from mongoengine.errors import ValidationError as MongoValidationError
from resources.errors import NotFoundError
from services.reseller_service import ResellerService
from .schemas.reseller_create_schema import ResellerCreateSchema
from .schemas.reseller_update_schema import ResellerUpdateSchema


class ResellerRouter(Resource):
    def __init__(self):
        self.resellerService = ResellerService()
        self.resellerCreateSchema = ResellerCreateSchema()
        self.resellerUpdateSchema = ResellerUpdateSchema()

    @jwt_required
    @authorize(["manager", "support"])
    def get(self, page=1, page_size=10, *args, **kwargs):
        try:
            resellers = self.resellerService.get(page, page_size)

            return ok(data=resellers)
        except Exception as e:
            return error()

    @jwt_required
    @authorize(["manager", "support"])
    def post(self, *args, **kwargs):
        json = request.get_json() or None
        if json is None:
            return bad_request()

        try:
            data = self.resellerCreateSchema.load(json)
            data["created_by"] = get_jwt_identity()
            data["updated_by"] = get_jwt_identity()
            for purchase in data["purchases"]:
                purchase["created_by"] = get_jwt_identity()

            reseller = self.resellerService.create(data)
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

    @jwt_required
    @authorize(["manager", "support"])
    def put(self, cpf: str, *args, **kwargs):
        json = request.get_json() or None
        if json is None:
            return bad_request()

        try:
            data = self.resellerUpdateSchema.load(json)
            data["updated_by"] = get_jwt_identity()

            reseller = self.resellerService.update(cpf, data)
        except NotFoundError:
            return bad_request("Reseller not found")
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

    @jwt_required
    @authorize(["manager", "support"])
    def delete(self, cpf: str, *args, **kwargs):
        try:
            self.resellerService.delete(cpf)
        except NotFoundError:
            return bad_request("Reseller not found")
        else:
            return ok()
