
from flask import jsonify
import models

def get_all_users():
    users = models.User.get_all()
    users_dict_list = []
    for user in users:
        users_dict_list.append(
            {'id': user.id,
             'firstname': user.firstname,
             'lastname': user.lastname,
             'username': user.username
             })

    return jsonify(users_dict_list)
