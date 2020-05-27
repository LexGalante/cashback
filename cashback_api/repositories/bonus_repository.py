from resources.errors import NotFoundError

import bson

from models.bonus import Bonus


class BonusRepository():
    def get(self):
        return Bonus.objects()

    def create(self, json: dict):

        bonus = Bonus(**json)
        bonus.save()

        return bonus

    def update(self, id: str, json: dict):
        bonus = Bonus.objects.get(
            id=bson.objectid.ObjectId(id))
        if bonus is None:
            raise NotFoundError(f"Bonus _id: {id} not found")

        for key, value in json.items():
            bonus[key] = value
        bonus.save()

        return bonus

    def delete(self, id: str, json: dict):
        bonus = Bonus.objects.get(
            id=bson.objectid.ObjectId(id))
        if bonus is None:
            raise NotFoundError(f"Bonus _id: {id} not found")
        else:
            bonus.delete()
