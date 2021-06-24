#!/usr/bin/python3
''' '''
import uuid
import datetime

class BaseModel():
    ''' '''
    def __init__(self):
        ''' '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        ''' '''
        return "[{}] ({}) {}". format(__class__.__name__, self.id, self.__dict__)

    def save(self):
        ''' '''
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        ''' '''
        dictionary = self.__dict__
        dictionary["__class__"] = __class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary

