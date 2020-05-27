# -*- coding: utf-8 -*-
from functools import wraps

from flask import jsonify, make_response

from flask_jwt_extended import (JWTManager, get_jwt_claims, get_jwt_identity,
                                verify_jwt_in_request)

from services.reseller_service import ResellerService


def authorize(roles):
    """
    Decorator to validate jwt token
    """
    def authorize_by_roles(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt_claims()
            if type(roles) in (list, tuple, set):
                for role in roles:
                    if role in claims["roles"]:
                        return fn(*args, **kwargs)
                else:
                    return jsonify({
                        "status": False,
                        "message": "Access denied"
                    }), 403
            elif roles in claims["roles"]:
                return fn(*args, **kwargs)
            else:
                return jsonify({
                    'status': False,
                    'message': "Access denied"
                }), 403
        return wrapper
    return authorize_by_roles


def configure_jwt(app):
    jwt = JWTManager(app)
    service = ResellerService()

    @jwt.user_claims_loader
    def add_claims_to_access_token(identity):
        reseller = service.get_by_cpf(identity)
        if reseller:
            return {
                'active': reseller.active,
                'roles': reseller.roles
            }

    @jwt.user_claims_loader
    def add_claims_to_access_token(identity):
        user = service.get_by_cpf(identity)
        return {'roles': user.roles}

    @jwt.expired_token_loader
    def expired_callback():
        return make_response(jsonify({
            'status': False,
            'sub_status': 1,
            'message': 'Token expirado'
        }), 401)

    @jwt.unauthorized_loader
    def unauthorized_callback(e):
        return make_response(jsonify({
            'status': False,
            'sub_status': 2,
            'description': e,
            'message': 'Credenciais Inválidas'
        }), 401)

    @jwt.claims_verification_loader
    def claims_verification_callback(e):
        return make_response(jsonify({
            'status': False,
            'sub_status': 3,
            'description': e,
            'message': 'Credenciais Inválidas'
        }), 401)

    @jwt.invalid_token_loader
    def invalid_token_loader_callback(e):
        return make_response(jsonify({
            'status': False,
            'sub_status': 4,
            'description': e,
            'message': 'Credenciais Inválidas'
        }), 401)

    @jwt.needs_fresh_token_loader
    def needs_fresh_token_callback(e):
        return make_response(jsonify({
            'status': False,
            'sub_status': 5,
            'description': e,
            'message': 'Credenciais Inválidas'
        }), 401)

    @jwt.revoked_token_loader
    def revoked_token_callback(e):
        return make_response(jsonify({
            'status': False,
            'sub_status': 6,
            'description': e,
            'message': 'Credenciais Inválidas'
        }), 401)

    @jwt.user_loader_callback_loader
    def user_loader_callback(e):
        return make_response(jsonify({
            'status': False,
            'sub_status': 6,
            'description': e,
            'message': 'Credenciais Inválidas'
        }), 401)

    @jwt.user_loader_error_loader
    def user_loader_error_callback(e):
        return make_response(jsonify({
            'status': False,
            'sub_status': 7,
            'description': e,
            'message': 'Credenciais Inválidas'
        }), 401)

    @jwt.token_in_blacklist_loader
    def token_in_blacklist_callback(e):
        return make_response(jsonify({
            'status': False,
            'sub_status': 8,
            'description': e,
            'message': 'Credenciais Inválidas'
        }), 401)

    @jwt.claims_verification_failed_loader
    def my_claims_verification_failed_callback(e):
        return make_response(jsonify({
            'status': False,
            'sub_status': 9,
            'description': e,
            'message': 'Credenciais Inválidas'
        }), 401)
