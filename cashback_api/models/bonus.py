from datetime import datetime

from mongoengine import (BooleanField, DateTimeField, StringField, FloatField)

from resources.database import mongo


class Bonus(mongo.Document):
    meta = {
        "collection": "bonus",
    }

    name = StringField(required=True, max_length=50)
    starting_margin = FloatField(
        required=True, min_value=0)
    final_margin = FloatField(required=True, min_value=0)
    bonus_percentage = FloatField(required=True, min_value=0, max_value=100)
    active = BooleanField(default=False)
    created_by = StringField(required=True)
    created_at = DateTimeField(default=datetime.now)
    updated_by = StringField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)
