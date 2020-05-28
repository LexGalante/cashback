from os import getenv
from flask_mongoengine import MongoEngine
from pymongo import MongoClient
from resources.configurations import configurations

mongo = MongoEngine()


def configure_mongo(app):
    """
    Configure mongo-engine
    """
    mongo.init_app(app)


def get_mongo():
    configuration_enviroment = getenv("FLASK_ENV") or "default"
    configuration = configurations[configuration_enviroment]
    client = MongoClient(configuration.MONGODB_HOST)
    database = client["cashback"]

    return database
