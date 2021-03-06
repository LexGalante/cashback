from marshmallow import Schema
from marshmallow.fields import Boolean, DateTime, Email, List, Str, Nested, Float, Int
from marshmallow.validate import Length
from resources.constants import SCHEMA_MESSAGE_REQUIRED


class ResellerPurchaseCreateSchema(Schema):
    code = Str(required=True, error_messages=SCHEMA_MESSAGE_REQUIRED)
    value = Float(required=True, error_messages=SCHEMA_MESSAGE_REQUIRED)
    date = DateTime(format='%Y-%m-%d %H:%M:%S', required=True,
                    error_messages=SCHEMA_MESSAGE_REQUIRED)
    status_code = Int(required=True)
    status_description = Str(required=True)


class ResellerCreateSchema(Schema):
    name = Str(required=True, error_messages=SCHEMA_MESSAGE_REQUIRED)
    last_name = Str(required=True, error_messages=SCHEMA_MESSAGE_REQUIRED)
    cpf = Str(required=True, validate=Length(max=11),
              error_messages=SCHEMA_MESSAGE_REQUIRED)
    email = Email(required=True, error_messages=SCHEMA_MESSAGE_REQUIRED)
    password = Str(required=True, error_messages=SCHEMA_MESSAGE_REQUIRED)
    active = Boolean(required=True, error_messages=SCHEMA_MESSAGE_REQUIRED)
    roles = List(Str(maxlenght=100), error_messages=SCHEMA_MESSAGE_REQUIRED)
    purchases = List(Nested(ResellerPurchaseCreateSchema))
