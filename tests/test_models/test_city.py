#!/usr/bin/python3
'''Testing file for the class City'''

import unittest
from models.city import City
import datetime


class TestCity(unittest.TestCase):
    '''Class to test the class City'''

    def test_init(self):
        '''Testing the creation of the class'''
        test = City()
        self.assertTrue(isinstance(test, City))
        self.assertTrue(hasattr(test, "id"))
        self.assertTrue(hasattr(test, "created_at"))
        self.assertTrue(hasattr(test, "updated_at"))
        test.name = "Holberton"
        self.assertEqual(test.name, "Holberton")

        test_dict = {"id": "ff02d7e0-4254-43b3-b867-d9decb0dda13",
                     "created_at": "2021-06-28T17:47:38.773238",
                     "updated_at": "2021-06-28T17:47:38.773248",
                     "__class__": "City"}
        test_1 = City(**test_dict)
        self.assertTrue(isinstance(test, City))
        self.assertEqual(test_1.id, "ff02d7e0-4254-43b3-b867-d9decb0dda13")
        self.assertEqual(test_1.created_at, datetime.datetime(
            2021, 6, 28, 17, 47, 38, 773238))
        self.assertEqual(test_1.updated_at, datetime.datetime(
            2021, 6, 28, 17, 47, 38, 773248))
        self.assertTrue(isinstance(test_1.id, str))
        self.assertTrue(isinstance(test_1.created_at, datetime.datetime))
        self.assertTrue(isinstance(test_1.updated_at, datetime.datetime))

        test_dict = {}
        test_3 = City(**test_dict)
        self.assertTrue(isinstance(test_3, City))
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
        test_1 = City()
        print(test_1)
        output = out.getvalue()

        test_1_dict = test_1.__dict__

        for key, value in test_1_dict.items():
            if type(value) == datetime.datetime:
                value = value.isoformat()
            else:
                self.assertIn(str(key), output)
                self.assertIn(str(value), output)

        str_test = "[City] ({})".format(test_1.id)
        self.assertIn(str_test, output)

    def test_save(self):
        '''Function to test the save instance method'''
        test_1 = City()
        update_1 = test_1.updated_at
        test_1.save()
        update_2 = test_1.updated_at
        self.assertNotEqual(update_1, update_2)

    def test_to_dict(self):
        '''Function to test the instance method to_dict'''

        test_1 = City()

        test_1_dict = test_1.to_dict()

        for key, value in test_1_dict.items():
            self.assertTrue(hasattr(test_1, key))

            if key == "created_at" or key == "updated_at":
                self.assertNotEqual(type(value), datetime.datetime)

        self.assertIn("__class__", test_1_dict.keys())

    def test_arguments(self):
        '''Funtion to test more arguments to the class City'''
        with self.assertRaises(TypeError):
            test = City()
            test.__str__("Perro")

        with self.assertRaises(TypeError):
            test.save("Perro")

        with self.assertRaises(TypeError):
            test.to_dict("Perro")

    def test_class_attributes(self):
        '''Function to test the class attributes'''
        self.assertTrue(hasattr(City, "name"))
        self.assertTrue(hasattr(City, "state_id"))
