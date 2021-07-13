from collections import UserList
from flask import Flask
from flask_restplus import Api, Resource
import csv
import os


from src.server.instance import server

app, api = server.app, server.api


class User(object):
    def __init__(self, id, name, email, password):
        self.__id = id
        self.__name = name
        self.__email = email
        self.__password = password

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

    def read_users(file):
        file_open = open(file, 'r')
        return csv.reader(file_open, delimiter=',')

    def new_user(file, user):
        file_open = open(file, 'w')
        c = csv.writer(file_open)
        c.writerow([user.id, user.name, user.email, user.password])
    
    
    def file_verification(): 
        route = 'file/users' 
        file = route + '/data.csv'

        if not os.path.exists(route): 
         os.makedirs(route)

        if not os.path.exists(file): 
         open(file, 'w')

        return file

    

