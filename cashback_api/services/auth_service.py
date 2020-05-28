from repositories.reseller_repository import ResellerRepository
from models.reseller import Reseller


class AuthService():
    def __init__(self):
        self.resellerRepository = ResellerRepository()

    def login(self, reseller: Reseller, password: str) -> bool:
        return self.resellerRepository.login(reseller, password)
