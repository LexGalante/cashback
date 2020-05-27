# -*- coding: utf-8 -*-
from datetime import timedelta
from os import getenv


class Configuration:
    SECRET_KEY = getenv('SECRET_KEY') or "CashbackSecret!"
    PORT = int(getenv('PORT', 5000))
    DEBUG = eval(getenv('DEBUG', False))
    MONGODB_HOST = getenv('MONGODB_URI')
    JSON_AS_ASCII = eval(getenv('JSON_AS_ASCII', False))
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(
        minutes=int(getenv('JWT_ACCESS_TOKEN_EXPIRES', 10))
    )
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(
        days=int(getenv('JWT_REFRESH_TOKEN_EXPIRES', 30))
    )


class TestingConfiguration(Configuration):
    FLASK_ENV = 'testing'
    TESTING = True


class DevelopmentConfiguration(Configuration):
    FLASK_ENV = 'development'
    DEBUG = True


class ProductionConfiguration(Configuration):
    FLASK_ENV = 'production'
    TESTING = False
    DEBUG = False


configurations = {
    'production': ProductionConfiguration,
    'testing': TestingConfiguration,
    'development': DevelopmentConfiguration,
    'default': DevelopmentConfiguration
}
