#!/usr/bin/python3
'''Testing file for the class BaseModel'''

import unittest
from models.base_model import BaseModel
import datetime


class Testbase(unittest.TestCase):
    '''Class to test the class BaseModel'''

    def test_init(self):
        '''Testing the creation of the class'''
        test = BaseModel()
        self.assertTrue(isinstance(test, BaseModel))
        self.assertTrue(hasattr(test, "id"))
        self.assertTrue(hasattr(test, "created_at"))
        self.assertTrue(hasattr(test, "updated_at"))
        test.name = "Holberton"
        self.assertEqual(test.name, "Holberton")

        test_dict = {"id": "ff02d7e0-4254-43b3-b867-d9decb0dda13", "created_at": "2021-06-28T17:47:38.773238",
                     "updated_at": "2021-06-28T17:47:38.773248", "__class__": "BaseModel"}
        test_1 = BaseModel(**test_dict)
        self.assertTrue(isinstance(test, BaseModel))
        self.assertEqual(test_1.id, "ff02d7e0-4254-43b3-b867-d9decb0dda13")
        self.assertEqual(test_1.created_at, datetime.datetime(2021, 6, 28, 17, 47, 38, 773238))
        self.assertEqual(test_1.updated_at, datetime.datetime(2021, 6, 28, 17, 47, 38, 773248))
        self.assertTrue(isinstance(test_1.id, str))
        self.assertTrue(isinstance(test_1.created_at, datetime.datetime))
        self.assertTrue(isinstance(test_1.updated_at, datetime.datetime))

        test_dict = {"__class__": "Perro"}
        test_2 = BaseModel(**test_dict)
        self.assertNotEqual(test_2.__class__, "Perro")
        
        test_dict = {}
        test_3 = BaseModel(**test_dict)
        self.assertTrue(isinstance(test_3, BaseModel))
        self.assertTrue(hasattr(test_3, "id"))
        self.assertTrue(hasattr(test_3, "created_at"))
        self.assertTrue(hasattr(test_3, "updated_at"))
        test_3.name = "Holberton"
        self.assertEqual(test_3.name, "Holberton")
        self.assertTrue(isinstance(test_3.id, str))
        self.assertTrue(isinstance(test_3.created_at, datetime.datetime))
        self.assertTrue(isinstance(test_3.updated_at, datetime.datetime))

    def test_str(self):
        ''' Function to test the __str__ instance method'''
        import sys
        from io import StringIO

        std_out = sys.stdout

        out = StringIO()
        sys.stdout = out
        test_1 = BaseModel()
        print(test_1)
        output = out.getvalue()

        test_1_dict = test_1.__dict__

        for key, value in test_1_dict.items():
            if type(value) == datetime.datetime:
                value = value.isoformat()
                print(type(output))
                self.assertIn(value, output)

            else:
                self.assertIn(str(key), output)
                self.assertIn(str(value), output)
    
        str_test = "[BaseModel] ({})".format(test_1.id)
        self.assertIn(str_test, output)