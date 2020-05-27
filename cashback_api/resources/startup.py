from flask import Flask

from resources.api import configure_api
from resources.configurations import configurations
from resources.jwt import configure_jwt
from resources.database import configure_mongo


def create_app(configuration_name: str) -> Flask:
    """ 
    Flask configurations
    Configure items:
        flask-restful
        jwt-manager
        mongo-engine
    """
    app = Flask(__name__)
    # load configuration
    app.config.from_object(configurations[configuration_name])
    # load flask restful
    configure_api(app)
    # load jwt
    configure_jwt(app)
    # load mongengine
    configure_mongo(app)

    return app
