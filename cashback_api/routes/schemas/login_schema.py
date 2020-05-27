from marshmallow import Schema
from marshmallow.fields import Str
from resources.constants import SCHEMA_MESSAGE_REQUIRED


class LoginSchema(Schema):
    cpf = Str(required=True, error_messages=SCHEMA_MESSAGE_REQUIRED)
    password = Str(required=True, error_messages=SCHEMA_MESSAGE_REQUIRED)
