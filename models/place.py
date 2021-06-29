#!/usr/bin/python3
''' This module declares the Place class. '''
from models.base_model import BaseModel


class Place(BaseModel):
    ''' This class creates the Place object.
    Attr:
        city_id (str): id of the city the place is in.
        user_id (str): id of the user.
        name (str): string with the name.
        description (str): description of the place.
        number_rooms (int): number of rooms in the place.
        number_bathrooms (int): number of bathrooms in the place.
        max_guest (int): maximum amount of guests in the place.
        price_by_night (int): price to stay for a night in the place.
        latitude (float): latitud of the place.
        longitude (float): longitud of the place.
        amenity_ids (list): id f the amenities.
    '''
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
        ''' Initialization of the attributes of the class and inherited. '''
        super().__init__(*args, **kwargs)

    def to_dict(self):
        ''' Create a dictionary with the attributes and add class, created at
        and updated at. '''
        dictionary = self.__dict__
        dictionary["__class__"] = __class__.__name__
        if "created_at" in dictionary and type(self.created_at) != str:
            dictionary["created_at"] = self.created_at.isoformat()
        if "updated_at" in dictionary and type(self.updated_at) != str:
            dictionary["updated_at"] = self.updated_at.isoformat()

        return dictionary

    def __str__(self):
        ''' Define the structure to print. '''
        msg = "[{}] ({}) {}".format(__class__.__name__, self.id, self.__dict__)
        return msg
