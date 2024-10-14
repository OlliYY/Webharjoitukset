import mysql
from flask import request, jsonify
import models

# products_controller.py sisältää tuotteiden CRUD-toiminnallisuudet.

def get_all_products():
    products = models.Product.get_all_products()
    return jsonify(products)


def create_product():
    data = request.get_json()
    name = data['name']
    description = data['description']

    models.Product.create_product(name, description)
    return jsonify({'message': 'Product created successfully!'}), 201


def update_product(product_id):
    data = request.get_json()
    name = data['name']
    description = data['description']

    models.Product.update_product(product_id, name, description)
    return jsonify({'message': 'Product updated successfully!'})


def delete_product(product_id):
    models.Product.delete_product(product_id)
    return jsonify({'message': 'Product deleted successfully!'})