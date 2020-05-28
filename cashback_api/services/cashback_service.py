import requests
from os import getenv
from datetime import datetime
from resources.errors import NotFoundError
from .reseller_service import ResellerService
from repositories.reseller_repository import ResellerRepository


class CashbackService():
    def __init__(self):
        self.resellerService = ResellerService()
        self.resellerRepository = ResellerRepository()

    def calcule_cashback(self, cpf: str) -> float:
        response = requests.get(f'{getenv("CASHBACK_GB_API")}?cpf={cpf}',
                                headers={'token': getenv("CASHBACK_API_TOKEN")})
        if response.status_code == 200:
            json = response.json()
            if "body" in json.keys() and "credit" in json.get("body"):
                return float(json["body"]["credit"])

        return 0

    def get_purchases(self, cpf: str):
        reseller = self.resellerService.get_by_cpf(cpf)
        if reseller is None:
            raise NotFoundError()

        return reseller.purchases

    def register_purchase(self, cpf: str, json: dict):
        reseller = self.resellerService.get_by_cpf(cpf)
        if reseller is None:
            raise NotFoundError()

        json["created_by"] = cpf
        json["created_at"] = datetime.now()
        json["status_code"] = 1 if "manager" in reseller.roles else 0
        json["status_description"] = "Aprovado" if "manager" in reseller.roles else "Em validação"
        json["cashback"] = self.get_cashback_by_value(json["value"])

        self.resellerRepository.add_purchase(reseller, json)

    def get_cashback_by_value(self, value: float) -> float:
        """
        Calculate cashback percentage
        """
        if value >= 1501:
            return 20.00
        elif value <= 1500 and value >= 1001:
            return 15.00
        else:
            return 10.00
