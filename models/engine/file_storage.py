#!/usr/Bin/python3
''' '''
import json
from models.base_model import BaseModel

class FileStorage():
    ''' '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        ''' '''
        return self.__objects

    def new(self, obj):
        ''' '''
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        ''' '''
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key]
        with open(self.__file_path, 'w') as file:
            json.dump(json_objects, file)

    def reload(self):
        ''' '''
        try:
            with open(self.__file_path, 'r') as file:
                json_objects = json.load(file)
            for key in json_objects:
                self.__objects[key] = json_objects[key]
        except:
            pass
