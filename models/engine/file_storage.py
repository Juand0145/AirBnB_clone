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
            FileStorage.__objects[key] = obj

    def save(self):
        ''' '''
        json_obj_dict = {}
        for key, value in FileStorage.__objects.items():
            json_obj_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as my_file:
            json.dump(json_obj_dict, my_file)

    
    def reload(self):
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        ''' '''
        try:
            with open(FileStorage.__file_path, 'r') as my_file:
                for key, value in json.load(my_file).items():
                    if key not in FileStorage.__objects:
                        class_create = value['__class__']
                        if class_create == 'BaseModel':
                            FileStorage.__objects[key] = BaseModel(**value)
                        elif class_create == 'User':
                            FileStorage.__objects[key] = User(**value)
                        elif class_create == 'State':
                            FileStorage.__objects[key] = State(**value)
                        elif class_create == 'City':
                            FileStorage.__objects[key] = City(**value)
        except:
            pass
