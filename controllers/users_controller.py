from flask import jsonify, request
import models

# users_controller.py sisältää käyttäjien CRUD-toiminnallisuudet.

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


def create_user():
    data = request.get_json()
    firstname = data['firstname']
    lastname = data['lastname']
    username = data['username']

    models.User.create_user(firstname, lastname, username)
    return jsonify({'message': 'User created successfully!'}), 201


def update_user(user_id):
    data = request.get_json()
    firstname = data['firstname']
    lastname = data['lastname']
    username = data['username']

    models.User.update_user(user_id, firstname, lastname, username)
    return jsonify({'message': 'User updated successfully!'})


def delete_user(user_id):
    models.User.delete_user(user_id)
    return jsonify({'message': 'User deleted successfully!'})
