#!/usr/bin/python3
''' '''
from models.base_model import BaseModel


class User(BaseModel):
    ''' '''
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_dict(self):
        ''' '''
        dictionary = self.__dict__
        dictionary["__class__"] = __class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary

    def __str__(self):
        ''' '''
        return "[{}] ({}) {}". format(__class__.__name__, self.id, self.__dict__)
