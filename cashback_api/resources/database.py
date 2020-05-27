from flask_mongoengine import MongoEngine

mongo = MongoEngine()


def configure_mongo(app):
    """
    Configure mongo-engine
    """
    mongo.init_app(app)
