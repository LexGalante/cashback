from datetime import datetime
from resources.errors import NotFoundError

from bcrypt import checkpw, gensalt, hashpw
from models.reseller import Reseller
from models.reseller_purchase import ResellerPurchase


class ResellerRepository():
    def __init__(self):
        self.default_fields = ["name", "last_name", "cpf", "email", "active",
                               "roles", "purchases", "created_by", "created_at", "updated_by", "updated_at"]

    def get(self, page: int, page_size: int, **kwargs):
        offset = (page - 1) * page_size
        fields = kwargs.get("fields") or self.default_fields
        if "all" in kwargs and kwargs.get("all"):
            return Reseller.objects().all()
        else:
            return Reseller.objects.skip(offset).limit(page_size).only(*fields).select_related()

    def get_by_cpf(self, cpf: str, **kwargs):
        fields = kwargs.get("fields") or self.default_fields

        return Reseller.objects(cpf=cpf).first()

    def create(self, json: dict):
        reseller = Reseller(**json)
        reseller.save()

        return reseller

    def update(self, cpf: str, json: dict):
        reseller = Reseller.objects(cpf=cpf).first()
        if reseller is None:
            raise NotFoundError(f"Reseller cpf: {cpf} not found")
        for key, value in json.items():
            reseller[key] = value
        reseller.save()

        return reseller

    def delete(self, cpf: str):
        reseller = Reseller.objects(cpf=cpf).first()
        if reseller is None:
            raise NotFoundError(f"Reseller cpf: {cpf} not found")
        else:
            reseller.delete()

    def login(self, reseller: Reseller, password: str) -> bool:
        return checkpw(password.encode('utf-8'), reseller.password.encode('utf-8'))

    def add_purchase(self, reseller: Reseller, json: dict):
        purchase = ResellerPurchase(**json)
        reseller.updated_by = reseller.cpf
        reseller.updated_at = datetime.now()
        reseller.purchases.append(purchase)

        reseller.save()
