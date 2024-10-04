import mysql.connector
from flask import Flask, jsonify

from controllers import users_controller

app = Flask(__name__)

"Testi testi testi"

""" Mikä tässä koodissa on vikana?

Jos tätä arvoidaan vain sillä perusteella, toimiiko kaikki, niin koodissa ei ole mitään vikaa, koska kaikki ominaisuudet
toimivat oikein

Arkkitehtuurin näkökulmasta koodi on aivan käyttökelvotonta.

Tehdään tämä seuraavaksi käyttäen MVC:tä.

"""


@app.route('/api/products')
def get_all_products():
    with mysql.connector.connect(user="root", database="sovelluskehykset_bad1", password="") as con:
        with con.cursor(dictionary=True) as cur:
            cur.execute("SELECT * FROM products")
            products = cur.fetchall()
            return jsonify(products)

app.add_url_rule('/api/users', view_func=users_controller.get_all_users)



if __name__ == '__main__':
    app.run()
