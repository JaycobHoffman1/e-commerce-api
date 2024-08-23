from __init__ import app, db
from flask import jsonify, request
from marshmallow import ValidationError
from models import Customer, CustomerAccount, Product, Order
from schemas import customer_schema, customer_account_schema, \
product_schema, products_schema, order_schema

# "Home" routes

@app.route('/')
def home():
    return 'Welcome to the E-commerce API!'

# "Customer" routes

@app.route('/customers', methods=['POST'])
def create_customer():
    try:
        customer_data = customer_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    new_customer = Customer(name=customer_data['name'], email=customer_data['email'], phone=customer_data['phone'])

    db.session.add(new_customer)
    db.session.commit()

    return jsonify({"message": "Customer added!"}), 201

@app.route('/customers/<int:id>', methods=['GET'])
def read_customer(id):
    customer = Customer.query.filter(Customer.id == id).first_or_404()

    return customer_schema.jsonify(customer)

@app.route('/customers/<int:id>', methods=['PUT'])
def update_customer(id):
    customer = Customer.query.get_or_404(id)

    try:
        customer_data = customer_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    customer.name = customer_data['name']
    customer.email = customer_data['email']
    customer.phone = customer_data['phone']

    db.session.commit()

    return jsonify({'message': 'Customer updated successfully!'}), 200

@app.route('/customers/<int:id>', methods=['DELETE'])
def delete_customer(id):
    customer = Customer.query.get_or_404(id)

    db.session.delete(customer)
    db.session.commit()

    return jsonify({'message': 'Customer removed successfully!'})

# "CustomerAccount" routes

@app.route('/customer_accounts', methods=['POST'])
def create_customer_account():
    try:
        customer_account_data = customer_account_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    new_customer_account = CustomerAccount(username=customer_account_data['username'], 
password=customer_account_data['password'], customer_id=customer_account_data['customer_id'])

    db.session.add(new_customer_account)
    db.session.commit()

    return jsonify({"message": "Customer account added!"}), 201

@app.route('/customer_accounts/<int:id>', methods=['GET'])
def read_customer_account(id):
    customer_account = CustomerAccount.query.filter(CustomerAccount.id == id).first_or_404()

    return customer_account_schema.jsonify(customer_account)

@app.route('/customer_accounts/<int:id>', methods=['PUT'])
def update_customer_account(id):
    customer_account = CustomerAccount.query.get_or_404(id)

    try:
        customer_account_data = customer_account_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    customer_account.username = customer_account_data['username']
    customer_account.password = customer_account_data['password']
    customer_account.customer_id = customer_account_data['customer_id']

    db.session.commit()

    return jsonify({'message': 'Customer account updated successfully!'}), 200

@app.route('/customer_accounts/<int:id>', methods=['DELETE'])
def delete_customer_account(id):
    customer_account = CustomerAccount.query.get_or_404(id)

    db.session.delete(customer_account)
    db.session.commit()

    return jsonify({'message': 'Customer account removed successfully!'})

# "Product" routes

@app.route('/products', methods=['POST'])
def create_product():
    try:
        product_data = product_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    new_product = Product(name=product_data['name'], price=product_data['price'])

    db.session.add(new_product)
    db.session.commit()

    return jsonify({"message": "Product added!"}), 201

@app.route('/products/<int:id>', methods=['GET'])
def read_product(id):
    product = Product.query.filter(Product.id == id).first_or_404()

    return product_schema.jsonify(product)

@app.route('/products', methods=['GET'])
def list_products():
    products = Product.query.all()

    return products_schema.jsonify(products)

@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get_or_404(id)

    try:
        product_data = product_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    product.name = product_data['name']
    product.price = product_data['price']

    db.session.commit()

    return jsonify({'message': 'Product updated successfully!'}), 200

@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)

    db.session.delete(product)
    db.session.commit()

    return jsonify({'message': 'Product removed successfully!'})

# "Order" routes

@app.route('/orders', methods=['POST'])
def place_order():
    try:
        order_data = order_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    new_order = Order(
order_date=order_data['order_date'],
delivery_date=order_data['delivery_date'],
customer_id=order_data['customer_id'],
product_id=order_data['product_id']
)

    db.session.add(new_order)
    db.session.commit()

    return jsonify({'message': 'Order placed!'})

@app.route('/orders/<int:id>', methods=['GET'])
def retrieve_order(id):
    order = Order.query.filter(Order.id == id).first_or_404()

    return order_schema.jsonify(order)

# ------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True) 