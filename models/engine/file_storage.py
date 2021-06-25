#!/usr/Bin/python3
''' '''
import json

class FileStorage():
    ''' '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        ''' '''
        return FileStorage.__objects

    def new(self, obj):
        ''' '''
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        ''' '''
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as my_file:
            json.dump(FileStorage.__objects, my_file)

    
    def reload(self):
        ''' '''
        try:
            with open(FileStorage.__file_path, 'r') as my_file:
                FileStorage.__objects = json.loads(my_file)

        except:
            pass

        # for key in json_objects:
        #     self.__objects[key] = json_objects[key]