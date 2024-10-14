import mysql.connector
from flask import Flask, jsonify

from controllers import users_controller, products_controller

app = Flask(__name__)

# !!Olen käyttänyt tehtävissä apuna tekoälyä!!
# app_harjoitus1.py sisältää kaikki tarvittavat reitit sekä käyttäjille että tuotteille.

"Testi testi testi"

""" Mikä tässä koodissa on vikana?

Jos tätä arvoidaan vain sillä perusteella, toimiiko kaikki, niin koodissa ei ole mitään vikaa, koska kaikki ominaisuudet
toimivat oikein

Arkkitehtuurin näkökulmasta koodi on aivan käyttökelvotonta.

Tehdään tämä seuraavaksi käyttäen MVC:tä.

"""


# USERS ROUTES
@app.route('/api/users', methods=['POST'])
def create_user():
    return users_controller.create_user()


@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    return users_controller.update_user(user_id)


@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return users_controller.delete_user(user_id)


app.add_url_rule('/api/users', view_func=users_controller.get_all_users)


# PRODUCTS ROUTES
@app.route('/api/products', methods=['GET'])
def get_all_products():
    return products_controller.get_all_products()


@app.route('/api/products', methods=['POST'])
def create_product():
    return products_controller.create_product()


@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    return products_controller.update_product(product_id)


@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    return products_controller.delete_product(product_id)


if __name__ == '__main__':
    app.run()
