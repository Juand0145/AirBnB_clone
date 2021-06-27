#!/usr/bin/python3
''' '''
from models.base_model import BaseModel


class Review(BaseModel):
    ''' '''
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        ''' '''
        super().__init__(*args, **kwargs)

    def to_dict(self):
        ''' '''
        dictionary = self.__dict__
        dictionary["__class__"] = __class__.__name__
        if "created_at" in dictionary and type(self.created_at) != str:
            dictionary["created_at"] = self.created_at.isoformat()
        if "updated_at" in dictionary and type(self.updated_at) != str:
            dictionary["updated_at"] = self.updated_at.isoformat()

        return dictionary

    def __str__(self):
        ''' '''
        msg = "[{}] ({}) {}".format(__class__.__name__, self.id, self.__dict__)
        return msg
