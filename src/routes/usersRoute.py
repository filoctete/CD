from flask import Flask, request, jsonify
from flask.json import JSONDecoder
from flask_restplus import Api, Resource
import csv
import json
import requests
from requests.models import ContentDecodingError

from src.server.instance import server
from src.controllers.user import User

app, api = server.app, server.api
file = 'src/routes/file/users/users.csv'

#file = User.file_verification
datas = User.read_users(file)
next(datas)
users = []
for row in datas:
    user = User(row[0], row[1], row[2], row[3], row[4])
    users.append({'id':user.id, 'name':user.name, 'email': user.email, 'password': user.password, 'id_group': user.id_group})

@app.route('/users', methods=['GET'])
def get():
    return jsonify(users)
    
@app.route('/users', methods=['POST'])
def post():
    content = request.json
    for x in content:
        id = x['id']
        name = x['name']
        email = x['email']
        password = x['password']
        id_group = x['id_group']
    users.append({'id': id, 'name': name, 'email': email, 'password': password, 'id_group': id_group})
    User.update_users(file, users)
    return jsonify(content)

@app.route('/users/remove_user/<user_id>', methods=['DELETE'])
def delete_id(user_id):		
    id = user_id		
    for user in users:
        if user['id'] == id:
            users.remove(user)
            break
    User.update_users(file, users)
    return jsonify(user_id)