#!/usr/bin/python3
''' This module declares the BaseModel class that is going to be the base for
other classes. '''
import uuid
import datetime
from models import storage


class BaseModel:
    ''' This class creates the BaseModel object.
    Attr:
        id (str): identification of the instance.
        created_at (datetime): date and time the instance was created.
        updated_at (datetime): date and time the instance was updated.
    '''

    def __init__(self, *args, **kwargs):
        ''' Initialization of the attributes of the class and inherited. '''
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)

            self.created_at = datetime.datetime.strptime(
                kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.datetime.strptime(
                kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        ''' Define the structure to print. '''
        msg = "[{}] ({}) {}".format(__class__.__name__, self.id, self.__dict__)
        return msg

    def save(self):
        ''' Rewrites the json file with the objects. '''
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        '''Create a dictionary with the attributes and add class, created at
        and updated at. '''
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = __class__.__name__
        if "created_at" in dictionary and type(self.created_at) != str:
            dictionary["created_at"] = self.created_at.isoformat()
        if "updated_at" in dictionary and type(self.updated_at) != str:
            dictionary["updated_at"] = self.updated_at.isoformat()

        return dictionary
