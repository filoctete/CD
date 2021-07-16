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
class Email(object):
    def __init__(self, id, id_user_source, id_user_destiny, subject, message, state):
        self.__id = id
        self.__id_user_source = id_user_source
        self.__id_user_destiny = id_user_destiny
        self.__subject = subject
        self.__message = message
        self.__state = state

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id
    
    @property
    def id_user_source(self):
        return self.__id_user_source

    @id_user_source.setter
    def id_user_source(self, id_source):
        self.__id_user_source = id_source
    
    @property
    def id_user_destiny(self):
        return self.__id_user_destiny

    @id_user_destiny.setter
    def id_user_destiny(self, id_user_destiny):
        self.__id_user_destiny = id_user_destiny
        
    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, subject):
        self.__subject = subject

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, message):
        self.__message = message
    
    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state):
        self.__state = state

    def read_emails(file):
        file_open = open(file, 'r')
        return csv.reader(file_open, delimiter=',')

    def update_emails(file, emails):
        file_open = open(file, 'w')
        c = csv.writer(file_open)
        c.writerow(['id','id_user_source', 'id_user_destiny', 'subject', 'message', 'state'])
        for email in emails:
            c.writerow([email['id'], email['id_user_source'], email['id_user_destiny'], email['subject'], email['message'], email['state']])

    def file_verification(): 
        route = 'src/routes/file/emails' 
        file = route + '/emails.csv'

        if not os.path.exists(route): 
            os.makedirs(route) 
        elif not os.path.isdir(route): 
            raise IOError(route + " nao eh um diretorio!")

        if not os.path.exists(file):    
             open(file, 'w')
        return file


    
