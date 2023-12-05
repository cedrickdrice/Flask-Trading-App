from marshmallow import Schema, fields

class CreateOrderSchema(Schema):
    stock_id = fields.Int(required=True)
    quantity = fields.Int(required=True)
    price = fields.Float(required=True)