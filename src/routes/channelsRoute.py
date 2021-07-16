from flask import Flask, request, jsonify
from flask.json import JSONDecoder
from flask_restplus import Api, Resource
import csv
import json
import requests
from requests.models import ContentDecodingError

from src.server.instance import server
from src.controllers.channel import Channel

app, api = server.app, server.api
file = 'src/routes/file/users/channels.csv'

#file = User.file_verification
datas = Channel.read_channel(file)
next(datas)
channels = []
for row in datas:
    channel = Channel(row[0], row[1])
    channels.append({'id':channel.id, 'name':channel.name})

@app.route('/channels', methods=['GET'])
def get_channel():
    return jsonify(channels)
    
@app.route('/channels', methods=['POST'])
def post_channel():
    content = request.json
    id = content['id']
    name = content['name']
    channels.append({'id': id, 'name': name})
    Channel.update_channels(file, channels)
    return jsonify(content)

@app.route('/channels/remove_channel/<id_channel>', methods=['DELETE'])
def delete_channel(id_channel):		
    id = id_channel		
    for channel in channels:
        if channel['id'] == id:
            channels.remove(channel)
            break
    Channel.update_channels(file,channels)
    return jsonify(id_channel)