import mysql

# models.py sisältää tietokantakyselyt sekä käyttäjille että tuotteille.

class User:
    def __init__(self, _id, firstname, lastname, username):
        self.id = _id
        self.firstname = firstname
        self.lastname = lastname
        self.username = username

    @staticmethod
    def get_all():
        with mysql.connector.connect(user="root", database="sovelluskehykset_bad1", password="") as con:
            with con.cursor(dictionary=True) as cur:
                cur.execute("SELECT * FROM users")
                users = cur.fetchall()
                users_list = []

                for user in users:
                    users_list.append(
                        User(user['id'], user['firstname'], user['lastname'], user['username'])
                    )

                return users_list

    @staticmethod
    def create_user(firstname, lastname, username):
        with mysql.connector.connect(user="root", database="sovelluskehykset_bad1", password="") as con:
            with con.cursor() as cur:
                cur.execute(
                    "INSERT INTO users (firstname, lastname, username) VALUES (%s, %s, %s)",
                    (firstname, lastname, username)
                )
                con.commit()

    @staticmethod
    def update_user(user_id, firstname, lastname, username):
        with mysql.connector.connect(user="root", database="sovelluskehykset_bad1", password="") as con:
            with con.cursor() as cur:
                cur.execute(
                    "UPDATE users SET firstname=%s, lastname=%s, username=%s WHERE id=%s",
                    (firstname, lastname, username, user_id)
                )
                con.commit()

    @staticmethod
    def delete_user(user_id):
        with mysql.connector.connect(user="root", database="sovelluskehykset_bad1", password="") as con:
            with con.cursor() as cur:
                cur.execute("DELETE FROM users WHERE id=%s", (user_id,))
                con.commit()


# PRODUCTS
class Product:
    @staticmethod
    def get_all_products():
        with mysql.connector.connect(user="root", database="sovelluskehykset_bad1", password="") as con:
            with con.cursor(dictionary=True) as cur:
                cur.execute("SELECT * FROM products")
                products = cur.fetchall()
                return products

    @staticmethod
    def create_product(name, description):
        with mysql.connector.connect(user="root", database="sovelluskehykset_bad1", password="") as con:
            with con.cursor() as cur:
                cur.execute(
                    "INSERT INTO products (name, description) VALUES (%s, %s)",
                    (name, description)
                )
                con.commit()

    @staticmethod
    def update_product(product_id, name, description):
        with mysql.connector.connect(user="root", database="sovelluskehykset_bad1", password="") as con:
            with con.cursor() as cur:
                cur.execute(
                    "UPDATE products SET name=%s, description=%s WHERE id=%s",
                    (name, description, product_id)
                )
                con.commit()

    @staticmethod
    def delete_product(product_id):
        with mysql.connector.connect(user="root", database="sovelluskehykset_bad1", password="") as con:
            with con.cursor() as cur:
                cur.execute("DELETE FROM products WHERE id=%s", (product_id,))
                con.commit()