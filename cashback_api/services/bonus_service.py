from repositories.bonus_repository import BonusRepository


class BonusService():
    def __init__(self):
        self.bonusRepository = BonusRepository()

    def get(self):
        return self.bonusRepository.get()

    def create(self, json: dict):
        if "active" not in json.keys():
            json["active"] = True

        return self.bonusRepository.create(json)

    def update(self, id: str, json: dict):
        return self.bonusRepository.update(id, json)

    def delete(self, id: str):
        return self.bonusRepository.delete(id)
