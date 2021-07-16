from flask import Flask, request, jsonify
from flask.json import JSONDecoder
from flask_restplus import Api, Resource
import csv
import json
import requests
from requests.models import ContentDecodingError

from src.server.instance import server
from src.controllers.group import Group

app, api = server.app, server.api
file = 'src/routes/file/users/groups.csv'

#file = User.file_verification
datas = Group.read_group(file)
next(datas)
groups = []
for row in datas:
    group = Group(row[0], row[1])
    groups.append({'id':group.id, 'name':group.name})

@app.route('/groups', methods=['GET'])
def get_group():
    return jsonify(groups)
    
@app.route('/groups', methods=['POST'])
def post_group():
    content = request.json
   # for x in content:
    id = content['id']
    name = content['name']
    groups.append({'id': id, 'name': name})
    Group.update_groups(file, groups)
    return jsonify(content)

@app.route('/groups/remove_group/<id_group>', methods=['DELETE'])
def delete_group(id_group):		
    id = id_group		
    for group in groups:
        if group['id'] == id:
            groups.remove(group)
            break
    Group.update_groups(file,groups)
    return jsonify(id_group)