from marshmallow import Schema, fields, validate

class LoginUserSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=6))