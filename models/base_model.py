#!/usr/bin/python3
''' '''
import uuid
import datetime
from models import storage


class BaseModel():
    ''' '''

    def __init__(self, *args, **kwargs):
        ''' '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

        if kwargs is not None:
            for key, value in kwargs.items():
                if key != "__class__":
                    self.key = value

            if "created_at" in kwargs:
                self.created_at = datetime.datetime.strptime(
                    kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            if "updated_at" in kwargs:
                self.updated_at = datetime.datetime.strptime(
                    kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")

        storage.new(self)

    def __str__(self):
        ''' '''
        return "[{}] ({}) {}". format(__class__.__name__, self.id, self.__dict__)

    def save(self):
        ''' '''
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        ''' '''
        dictionary = self.__dict__
        dictionary["__class__"] = __class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
