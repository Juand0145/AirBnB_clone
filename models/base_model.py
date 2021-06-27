#!/usr/bin/python3
''' '''
import uuid
import datetime
from models import storage


class BaseModel():
    ''' '''

    def __init__(self, *args, **kwargs):
        ''' '''
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)

            if "created_at" in kwargs:
                self.created_at = datetime.datetime.strptime(
                    kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            if "updated_at" in kwargs:
                self.updated_at = datetime.datetime.strptime(
                    kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        ''' '''
        msg = "[{}] ({}) {}".format(__class__.__name__, self.id, self.__dict__)
        return msg

    def save(self):
        ''' '''
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        ''' '''
        dictionary = self.__dict__
        dictionary["__class__"] = __class__.__name__
        if "created_at" in dictionary and type(self.created_at) != str:
            dictionary["created_at"] = self.created_at.isoformat()
        if "updated_at" in dictionary and type(self.updated_at) != str:
            dictionary["updated_at"] = self.updated_at.isoformat()

        return dictionary
