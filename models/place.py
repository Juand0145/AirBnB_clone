#!/usr/bin/python3
''' '''
from models.base_model import BaseModel

class Place(BaseModel):
    ''' '''
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

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
        return "[{}] ({}) {}". format(__class__.__name__, self.id, self.__dict__)
