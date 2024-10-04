import mysql


class User:
    def __init__(self,_id, firstnaem, lastname, username):
        self.id = _id
        self.firstname = firstnaem
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