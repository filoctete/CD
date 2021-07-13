from flask import Flask
from flask_restplus import Api, Resource


from src.server.instance import server

app, api = server.app, server.api

users = [{'name':'admin','email':'admin@admin.pt','password':'12qwaszx,.','user_type':0}]
books_db = [
    {'id': 0, 'title': 'war of peace'}
    ]

@api.route('/books/ola')
class BookList(Resource):
    def get(self, ):
        return books_db
        
    def post(self, ):
        response = api.payload
        books_db.append(response)
        return response, 200