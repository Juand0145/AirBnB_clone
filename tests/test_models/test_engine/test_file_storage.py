#!/usr/bin/python3
"""Testing file for the class FileStorage"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    '''Class to test the class FileStorage'''

    def setUp(self):
        ''' Function to setup the testing '''
        self.storage = FileStorage()

    def test_all(self):
        '''Testing function to check the instance method all'''
        file = FileStorage()
        test = BaseModel()
        self.assertFalse(len(file.all()) <= 0)

    def test_new(self):
        '''Testing function to check the instance method new'''
        # file = FileStorage()
        # object_1 = file.all()

        # test = BaseModel()
        # file.new(test)
        # object_2 = file.all()
        # self.assertNotEqual(object_1, object_2)
        pass

    def test_save(self):
        '''Testing function to check the instance method save'''
        self.assertEqual(self.storage.save(), None)

    def test_reload(self):
        '''Testing function to check the instance method reload'''
        pass
