# -*- coding: utf-8 -*-
from flask import request

from flask_jwt_extended import (create_access_token, create_refresh_token,
                                get_jwt_identity, jwt_refresh_token_required)
from flask_restful import Resource
from marshmallow.exceptions import ValidationError as SchemaValidationError
from mongoengine.errors import NotUniqueError
from mongoengine.errors import ValidationError as MongoValidationError
from resources.errors import NotFoundError
from resources.http_response import bad_request, error, ok
from services.auth_service import AuthService
from services.reseller_service import ResellerService

from .schemas.login_schema import LoginSchema
from .schemas.reseller_register_schema import ResellerRegisterSchema


class AuthRouter(Resource):
    def __init__(self):
        self.resellerService = ResellerService()
        self.authService = AuthService()

    def post(self, *args, **kwargs):
        json = request.get_json() or None
        if json is None:
            return bad_request()
        try:
            data = LoginSchema().load(json)
            reseller = self.resellerService.get_by_cpf(data["cpf"])
            if reseller == None:
                return bad_request(f'Reseller: {data["cpf"]} not found, please register before to tryng login')
            if not reseller.active:
                return bad_request(f'Reseller: {data["cpf"]} are disabled')
            if not self.authService.login(reseller, data["password"]):
                return bad_request("Check username and password")
            jwt = {
                'token': create_access_token(identity=reseller.cpf),
                'refresh': create_refresh_token(identity=reseller.cpf)
            }
            return ok(data=jwt)
        except NotFoundError:
            return bad_request('Reseller not found')
        except SchemaValidationError as e:
            return bad_request(errors=e.messages)
        except Exception as e:
            return error(e)


class AuthRefreshRouter(Resource):
    @jwt_refresh_token_required
    def post(self, *args, **kwargs):
        return ok(data={'token': create_access_token(identity=get_jwt_identity())})


class AuthRegisterRouter(Resource):
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
        except NotUniqueError as e:
            return bad_request("This email OR cpf already exist")
        except MongoValidationError as e:
            return bad_request('Error storage', e.message)
        except SchemaValidationError as e:
            return bad_request('Invalid request', e.messages)
        except Exception as e:
            return error(e)
        else:
            return ok(data=reseller)
