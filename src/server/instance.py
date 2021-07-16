from flask import Flask
from flask_restplus import Api
from flask_socketio import *
from flask_socketio import *
#from src.controllers.users import User

import os


class Server():
    def __init__(self, ):
        self.app = Flask(__name__)
        self.api = Api(self.app,
                    version= '1.0',
                    title='qwerty',
                    description='qwf',
                    doc='/docs',
            )
        self.socketio = SocketIO(self.app, cors_allowed_origins='*')
    def run(self, ):
        self.app.run(
            debug=True
        )
server = Server()
