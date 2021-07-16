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
class Channel(object):
    def __init__(self, id, name):
        self.__id = id
        self.__name = name

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

    def read_channel(file):
        file_open = open(file, 'r')
        return csv.reader(file_open, delimiter=',')

    def update_channels(file, channels):
        file_open = open(file, 'w')
        c = csv.writer(file_open)
        c.writerow(['id', 'name'])
        for channel in channels:
            c.writerow([channel['id'], channel['name']])

    def file_verification(): 
        route = 'src/routes/file/channels' 
        file = route + '/channels.csv'

        if not os.path.exists(route): 
            os.makedirs(route) 
        elif not os.path.isdir(route): 
            raise IOError(route + " nao eh um diretorio!")

        if not os.path.exists(file):    
             open(file, 'w')
        return file


    
