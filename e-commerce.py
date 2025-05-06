from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data storage
products = []
users = []
orders = []

# Models
class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

class Order:
    def __init__(self, order_id, user_id, product_id, quantity):
        self.order_id = order_id
        self.user_id = user_id
        self.product_id = product_id
        self.quantity = quantity

# Routes
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify([product.__dict__ for product in products])

@app.route('/products', methods=['POST'])
def add_product():
    data = request.json
    product = Product(len(products) + 1, data['name'], data['price'], data['stock'])
    products.append(product)
    return jsonify(product.__dict__), 201

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify([user.__dict__ for user in users])

@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    user = User(len(users) + 1, data['name'], data['email'])
    users.append(user)
    return jsonify(user.__dict__), 201

@app.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    order = Order(len(orders) + 1, data['user_id'], data['product_id'], data['quantity'])
    
    # Check product stock
    product = next((p for p in products if p.product_id == order.product_id), None)
    if not product or product.stock < order.quantity:
        return jsonify({'error': 'Not enough stock or product not found'}), 400
    
    # Deduct stock
    product.stock -= order.quantity
    orders.append(order)
    return jsonify(order.__dict__), 201

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify([order.__dict__ for order in orders])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
