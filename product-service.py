from flask import Flask, jsonify
import requests
app = Flask(__name__)

products = [
    {"id": 1, "name": "Pineapple", "price": 2.25, "quantity": 1000},
    {"id": 2, "name": "Toothpaste", "price": 1.25, "quantity": 5000},
    {"id": 3, "name": "Essential Oils", "price": 10.99, "quantity": 250}

]
# Endpoint 1: List products 
@app.route('/https://four55-product-service.onrender.com', methods=['GET'])
def retrieve_products():
    return jsonify(products)

#Endpint 2: get product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return jsonify(product)
    else:
        return jsonify({"message": "Product not found"}), 404
    
#Endpoint 3: Allow the addition of new products 
@app.route('/products', methods=['POST'])
def add_new_product():
    data = requests.get_json()
    if 'name' in data and 'price' in data and 'quantity' in data:
        new_product = {
            "id": len(products) + 1,
            "name": data['name'],
            "price": data['price'],
            "quantity": data['quantity']
        }
        products.append(new_product)
        return jsonify(new_product), 201
    
if __name__ == '__main__':
    app.run(debug=True)
