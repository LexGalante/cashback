from datetime import datetime
from bcrypt import gensalt, hashpw
from repositories.reseller_repository import ResellerRepository


class ResellerService():
    def __init__(self):
        self.resellerRepository = ResellerRepository()

    def get(self, page: int, page_size: int):
        return self.resellerRepository.get(page, page_size)

    def get_by_cpf(self, cpf: str):
        return self.resellerRepository.get_by_cpf(cpf)

    def create(self, json: dict, **kwargs):
        json["created_at"] = datetime.now()
        json["password"] = hashpw(
            json["password"].encode('utf-8'), gensalt(12))

        if "active" not in json.keys():
            json["active"] = True
        if "register" in kwargs and kwargs.get("register"):
            json["created_by"] = "default"
            json["updated_by"] = "default"
            json["roles"] = ["default"]
        if len(json["roles"]) == 0:
            json["roles"] = ["default"]

        reseller = self.resellerRepository.create(json)
        reseller["password"] = None

        return reseller

    def update(self, cpf: str, json: dict):
        if "purchases" in json.keys() and len(json["purchases"]) == 0:
            del json["purchases"]

        json["updated_at"] = datetime.now()
        reseller = self.resellerRepository.update(cpf, json)
        reseller["password"] = None

        return reseller

    def delete(self, cpf: str):
        return self.resellerRepository.delete(cpf)
