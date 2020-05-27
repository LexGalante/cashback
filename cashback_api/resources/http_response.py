from flask import Response, jsonify, make_response


def ok(message="Sucesso", data={}):
    """HTTP Response 200"""
    return make_response(jsonify({
        'status': True,
        'message': message,
        'data': data
    }), 200)


def created(message="", data={}):
    """HTTP Response 201"""
    return make_response(jsonify({
        'status': True,
        'message': message,
        'data': data
    }), 200)


def no_content():
    """HTTP Response 204"""
    return Response(status=204)


def bad_request(message='Ocorreram erros verifique', errors={}):
    """HTTP Response 400"""
    return make_response(jsonify({
        'status': False,
        'message': message,
        'data': errors
    }), 400)


def unathorized():
    """HTTP Response 401"""
    return make_response(jsonify({
        'status': False,
        'message': 'Sem autorização',
    }), 401)


def error(message='Ocorreu um erro inesperado', e=None):
    """HTTP Response 500"""
    return make_response(jsonify({
        'status': False,
        'message': str(message),
        'data': str(e)
    }), 500)
