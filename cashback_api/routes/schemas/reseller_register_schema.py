from marshmallow import Schema
from marshmallow.fields import Boolean, DateTime, Email, List, Str
from marshmallow.validate import Length
from resources.constants import SCHEMA_MESSAGE_REQUIRED


class ResellerRegisterSchema(Schema):
    name = Str(required=True, error_messages=SCHEMA_MESSAGE_REQUIRED)
    last_name = Str(required=True, error_messages=SCHEMA_MESSAGE_REQUIRED)
    cpf = Str(required=True, validate=Length(max=11),
              error_messages=SCHEMA_MESSAGE_REQUIRED)
    email = Email(required=True, error_messages=SCHEMA_MESSAGE_REQUIRED)
    password = Str(required=True, error_messages=SCHEMA_MESSAGE_REQUIRED)
