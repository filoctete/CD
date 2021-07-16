
from flask import Flask
from flask_restplus import Api, Resource
import csv
import os
import json
from json import JSONEncoder
import numpy
from dataclasses import dataclass
from dataclasses_json import dataclass_json
import pandas as pd


from src.server.instance import server

app, api = server.app, server.api

@dataclass_json
@dataclass
class User(object):
    def __init__(self, id, name, email, password, id_group):
        self.__id = id
        self.__name = name
        self.__email = email
        self.__password = password
        self.__id_group = id_group

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id
        
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email
    
    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def id_group(self):
        return self.__id_group

    @id_group.setter
    def id_group(self, id_group):
        self.__id_group = id_group

    def read_users(file):
        file_open = open(file, 'r')
        return csv.reader(file_open, delimiter=',')

    def update_users(file, users):
        file_open = open(file, 'w')
        c = csv.writer(file_open)
        c.writerow(['id', 'name', 'email', 'password', 'id_group'])
        for user in users:
            c.writerow([user['id'], user['name'], user['email'], user['password'], user['id_group']])

    def file_verification(): 
        route = 'src/routes/file/users' 
        file = route + '/users.csv'

        if not os.path.exists(route): 
            os.makedirs(route) 
        elif not os.path.isdir(route): 
            raise IOError(route + " nao eh um diretorio!")

        if not os.path.exists(file):    
             open(file, 'w')
        return file


    
