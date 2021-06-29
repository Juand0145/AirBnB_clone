#!/usr/Bin/python3
'''Is a class FileStorage that serializes instances
to a JSON file and deserializes JSON file to instances:'''
import json


class FileStorage:
    '''Is a class FileStorage that serializes instances
    to a JSON file and deserializes JSON file to instances:'''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''Instance Method that returns the dictionary __objects '''
        return FileStorage.__objects

    def new(self, obj):
        '''Is apublic instance that sets in __objects
        the obj with key <obj class name>.id'''
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        '''Is a public instance that serializes __objects to the
        JSON file (path: __file_path)'''
        json_obj_dict = {}
        for key, value in FileStorage.__objects.items():
            json_obj_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as my_file:
            json.dump(json_obj_dict, my_file)

    def reload(self):
        '''Is a instance method deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)'''
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
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
                        elif class_create == 'Amenity':
                            FileStorage.__objects[key] = Amenity(**value)
                        elif class_create == 'Place':
                            FileStorage.__objects[key] = Place(**value)
                        elif class_create == 'Review':
                            FileStorage.__objects[key] = Review(**value)
        except:
            pass
