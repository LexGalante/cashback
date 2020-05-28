import sys
import json
import pytest
from dotenv import load_dotenv
from os.path import dirname, isfile, join
from os.path import dirname as d
from os.path import abspath, join
root_dir = d(d(abspath(__file__)))
sys.path.append(root_dir)

# a partir do arquivo atual adicione ao path o arquivo .env
_ENV_FILE = join(dirname(__file__), "../.env")

# existindo o arquivo faça a leitura do arquivo através da função load_dotenv
if isfile(_ENV_FILE):
    load_dotenv(dotenv_path=_ENV_FILE)


@pytest.fixture(scope="session")
def client():
    from resources.startup import create_app
    app = create_app("testing")
    context = app.app_context()
    context.push()
    yield app.test_client()
    context.pop()


@pytest.fixture(scope="function")
def authorization(client):
    """ 
    Provider JWT token
    """
    response = client.post("/api/v1/auth",
                           data=json.dumps({
                               "cpf": "06909142969",
                               "password": "123456"
                           }),
                           headers={
                               "Content-Type": "application/json",
                               "Accept": "application/json"
                           })
    jwt = json.loads(response.data)
    return jwt["data"]


@pytest.fixture(scope="function")
def authorization_without_permission(client):
    """ 
    Provider JWT token
    """
    response = client.post("/api/v1/auth",
                           data=json.dumps({
                               "cpf": "15350946057",
                               "password": "123456"
                           }),
                           headers={
                               "Content-Type": "application/json",
                               "Accept": "application/json"
                           })
    jwt = json.loads(response.data)
    return jwt["data"]


@pytest.fixture(scope='function')
def get_reseller_repository():
    from repositories.reseller_repository import ResellerRepository

    return ResellerRepository()


@pytest.fixture(scope='function')
def get_auth_service():
    from services.auth_service import AuthService

    return AuthService()


@pytest.fixture(scope='function')
def get_cashback_service():
    from services.cashback_service import CashbackService

    return CashbackService()


@pytest.fixture(scope='function')
def get_reseller_service():
    from services.reseller_service import ResellerService

    return ResellerService()


@pytest.fixture(scope="function")
def clean_reseller():
    def clean(cpf: str):
        """
        Clean reseller from database test
        """
        from services.reseller_service import ResellerService

        service = ResellerService()
        service.delete(cpf)
    return clean
