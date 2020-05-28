from datetime import datetime

from mongoengine import (DateTimeField, EmbeddedDocument, IntField,
                         EmbeddedDocumentField, FloatField, StringField)

from resources.database import mongo


class ResellerPurchase(mongo.EmbeddedDocument):
    code = StringField(required=True, max_length=20)
    value = FloatField(required=True, min_value=0)
    date = DateTimeField(required=True, default=datetime.now)
    status_code = IntField(required=True, default=0)
    status_description = StringField(
        required=True, max_length=50, default="In Validation")
    created_by = StringField(required=True)
    created_at = DateTimeField(default=datetime.now)
    cashback = FloatField(required=True, min_value=0, max_value=100)
