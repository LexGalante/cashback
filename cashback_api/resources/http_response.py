from flask import Response, jsonify, make_response
from resources.logger import log_info, log_error, log_warning


def ok(message="Sucesso", data={}):
    """HTTP Response 200"""
    return make_response(jsonify({
        'status': True,
        'message': message,
        'data': data
    }), 200)


def created(message="", data={}):
    log_info("created new entity")
    """HTTP Response 201"""
    return make_response(jsonify({
        'status': True,
        'message': message,
        'data': data
    }), 200)


def no_content():
    log_warning("no content resource trigerred")
    """HTTP Response 204"""
    return Response(status=204)


def bad_request(message='ops!!!', errors={}):
    log_warning(f'{message}, {errors}')
    """HTTP Response 400"""
    return make_response(jsonify({
        'status': False,
        'message': message,
        'data': errors
    }), 400)


def unathorized():
    log_warning("Attempt to access resource without authorization")
    """HTTP Response 401"""
    return make_response(jsonify({
        'status': False,
        'message': 'Unathorized',
    }), 401)


def error(message='ops!!!', e=None):
    log_warning(f'{message}, {str(e)}')
    """HTTP Response 500"""
    return make_response(jsonify({
        'status': False,
        'message': str(message),
        'data': str(e)
    }), 500)
