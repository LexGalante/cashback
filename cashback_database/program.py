from time import sleep
from os import getenv
from os import getenv
from os.path import dirname
from os.path import isfile
from os.path import join
from pymongo import MongoClient
from dotenv import load_dotenv
from seeds.reseller_seed import seed_resellers


# aguardamos 30 segundos para iniciar a rotina
print("Seed started waiting 30 seconds...")
sleep(30)
# a partir do arquivo atual adicione ao path o arquivo .env
_ENV_FILE = join(dirname(__file__), '.env')

# existindo o arquivo faça a leitura do arquivo através da função load_dotenv
if isfile(_ENV_FILE):
    load_dotenv(dotenv_path=_ENV_FILE)

mongo = MongoClient(getenv("MONGODB_URI"))
databases = mongo.list_database_names()
if "cashback" not in databases:
    print("Structure doesnt exist, creating this structure...")
    try:
        cashback = mongo["cashback"]
        seed_resellers(cashback)
        print("filled initial resellers")
    except:
        print("Error on database create and seed")

if "cashback_test" not in databases:
    print("Test Structure doesnt exist, creating this test structure...")
    try:
        cashback = mongo["cashback_test"]
        seed_resellers(cashback)
        print("filled initial resellers")
    except:
        print("Error on test database create and seed")
