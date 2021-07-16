from flask import Flask, request, jsonify
from flask.json import JSONDecoder
from flask_restplus import Api, Resource
import csv
import json
import requests
from requests.models import ContentDecodingError

from src.server.instance import server
from src.controllers.email import Email

app, api = server.app, server.api
file = 'src/routes/file/users/emails.csv'

#file = User.file_verification
datas = Email.read_emails(file)
next(datas)
emails = []
for row in datas:
    email = Email(row[0], row[1], row[2], row[3], row[4], row[5])
    emails.append({'id':email.id, 'id_user_source':email.id_user_source, 'id_user_destiny':email.id_user_destiny,'subject': email.subject, 'message': email.message, 'state': email.state})

@app.route('/email', methods=['GET'])
def get_email():
    return jsonify(emails)
    
@app.route('/emails', methods=['POST'])
def post_email():
    content = request.json
    for x in content:
        id = x['id']
        id_user_source = x['id_user_source']
        id_user_destiny = x['id_user_destiny']
        subject = x['subject']
        message = x['message']
        state = x['state']
    emails.append({'id': id,'id_user_source': id_user_source,'id_user_destiny': id_user_destiny, 'subject': subject, 'message': message, 'state': state})
    Email.update_emails(file, emails)
    return jsonify(content)

@app.route('/emails/remove_email/<id_email>', methods=['DELETE'])
def delete_id_email(id_email):		
    id = id_email		
    for email in emails:
        if email['id'] == id:
            emails.remove(email)
    Email.update_emails(file, emails)
    return jsonify(id_email)

#metodo get que retorna todos as mensagens/emails com destino a um determinado user
#emails a listar na caixa de mensagens de um user
@app.route('/email/<id_user_destiny>', methods=['GET'])
def get_emails_user_destiny(id_user_destiny):
    id = id_user_destiny
    emails_user = []
    for email in emails:
        if email['id_user_destiny'] == id:
            emails_user.append(email)
    return jsonify(emails_user)