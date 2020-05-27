from .reseller_service import ResellerService


class CashbackService():
    def __init__(self):
        self.resellerService = ResellerService()

    def calcule_cashback(self, cpf: str):
        pass

    def get_purchases(self, cpf: str):
        pass

    def register_purchase(self, cpf: str, json: dict):
        pass
