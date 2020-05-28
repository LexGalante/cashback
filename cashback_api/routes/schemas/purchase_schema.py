from marshmallow import Schema
from marshmallow.fields import Boolean, DateTime, Email, List, Str, Nested, Float, Int
from marshmallow.validate import Length
from resources.constants import SCHEMA_MESSAGE_REQUIRED


class PurchaseSchema(Schema):
    code = Str(required=True, error_messages=SCHEMA_MESSAGE_REQUIRED)
    value = Float(required=True, error_messages=SCHEMA_MESSAGE_REQUIRED)
    date = DateTime(format='%Y-%m-%d %H:%M:%S', required=True,
                    error_messages=SCHEMA_MESSAGE_REQUIRED)
