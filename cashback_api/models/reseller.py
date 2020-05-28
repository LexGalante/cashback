from datetime import datetime

from mongoengine import (BooleanField, DateTimeField, EmailField,
                         EmbeddedDocumentListField, IntField, ListField,
                         StringField)

from resources.database import mongo
from models.reseller_purchase import ResellerPurchase


class Reseller(mongo.Document):
    meta = {
        "collection": "resellers",
        "ordering": ["cpf"]
    }

    name = StringField(required=True, max_length=50)
    last_name = StringField(required=False, max_length=150)
    cpf = StringField(required=False, max_length=11, unique=True)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)
    active = BooleanField(default=False)
    roles = ListField(StringField(max_length=100), default=[])
    purchases = EmbeddedDocumentListField(document_type=ResellerPurchase)
    created_by = StringField(required=True)
    created_at = DateTimeField(default=datetime.now)
    updated_by = StringField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)
