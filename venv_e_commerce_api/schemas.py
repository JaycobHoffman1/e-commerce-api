from __init__ import ma
from marshmallow import fields

class CustomerSchema(ma.Schema):
    name = fields.String(required=True)
    email = fields.String(required=True)
    phone = fields.String(required=True)

    class Meta:
        fields = ('id', 'name', 'email', 'phone')

class CustomerAccountSchema(ma.Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)
    customer_id = fields.Integer(required=True)

    class Meta:
        fields = ('id', 'username', 'password', 'customer_id')

class ProductSchema(ma.Schema):
    name = fields.String(required=True)
    price = fields.Float(required=True)

    class Meta:
        fields = ('id', 'name', 'price')

class OrderSchema(ma.Schema):
    order_date = fields.Date(required=True)
    delivery_date = fields.Date(required=True)
    customer_id = fields.Integer(required=True)
    product_id = fields.Integer(required=True)

    class Meta:
        fields = ('id', 'order_date', 'delivery_date', 'customer_id', 'product_id')

# Initializing schemas

customer_schema = CustomerSchema()
customer_account_schema = CustomerAccountSchema()
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
order_schema = OrderSchema()