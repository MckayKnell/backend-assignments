from flask import Flask


product_records = [{
        "product_id": "1",
        "product_name": "Hasbro Gaming Clue Game",
        "description": "One murder... 6 suspects...",
        "price": 9.95,
        "active" : True
    }

    {
        "product_id": "2",
        "product_name": "Monopoly Board Game The Classic Edition, 2-8 players",
        "description" : "Relive the Monopoly experiences...", 
        "price": 35.50
        "active": False
    }
]


@app.route('/product', methods=['POST'])
def add_product():
    data = request.form if request.form else request.json
    product = {}

    product['product_id'] = data['product_id']
    product['name'] = data['name']
    product['description'] = data['description']
    product['price'] = data['price']
    product['active'] =data['active']

    product_records.append(product)

    return jsonify({'message': 'product added', 'results': product}), 201


@app.route('/products', methods=['GET'])
def get_all_products():
    return jsonify({'message': 'products found', 'results': product_records}), 200

@app.route('/product/active', methods=['GET'])
def get_active():
    for product in product_records:
        if product['active'] == bool('True'):
            return jsonify({'message': 'products found', 'results': product}),200
    return jsonify({'message':'No Active Products found' }), 404

@app.route('/products/<product_id>', methods=['GET'])
def read_products_by_id(product_id):
    for product in product_records:
        if product['product_id'] == int(product_id):
            return jsonify({"message": "products found", "results": product}), 200
    return jsonify({"message": f'Product with id {product_id} not found.'}), 404



@app.route('/product/<product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.form if request.form else request.json

    product = {}

    for record in product_records:
        if product['product_id'] == int(product_id):
            product = record

    product['name'] = data.get('name', product['name'])
    product['description'] = data.get('description', product['description'])
    product['price'] = data.get('price', product['price'])

    return jsonify({'message': 'products updated', 'results': product}), 200

@app.route('/product/delete/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    for product in product_records:
        if product['product_id'] == int(product_id):
            return jsonify({'message': 'product deleted'}),405
    return jsonify({'message': 'Product not found'}), 404

# or

@app.route('/product/delete/<product_id>', methods=['PUT'])
def delete_product(product_id):
    data = request.form if request.form else request.json

    product = {}

    for record in product_records:

        if product['product_id'] == int[product_id]:
            product = record
    
    product['active'] = data.get('active', product['active'])
           

    return jsonify({'message': 'Record doesnt exist'}), 404




if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8086')
