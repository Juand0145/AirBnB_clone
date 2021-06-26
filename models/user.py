#!/usr/bin/python3
''' '''
from base_model import BaseModel


class User(BaseModel):
    ''' '''
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self):
        super().__init__()

my_user = User()
my_user.first_name = "Betty"
my_user.last_name = "Holberton"
my_user.email = "airbnb@holbertonshool.com"
my_user.password = "root"
print(my_user)
