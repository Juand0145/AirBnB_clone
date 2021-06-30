#!/usr/bin/python3
"""Testing file for the class FileStorage"""
import unittest
import json
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
        file = FileStorage()
        dictionary = {"id": "64a8e9f5-4840-431c-9305-baff80edd778",
                      "created_at": "2021-06-30T10:45:57.274432",
                      "updated_at": "2021-06-30T10:45:57.274432"}
        instance = BaseModel(**dictionary)
        file.new(instance)
        objects = file.all()
        self.assertTrue(
            "BaseModel.64a8e9f5-4840-431c-9305-baff80edd778" in objects.keys())

    def test_save(self):
        '''Testing function to check the instance method save'''
        dictionary = {"id": "64a8e9f5-4840-431c-9305-baff80edd778",
                      "created_at": "2021-06-30T10:45:57.274432",
                      "updated_at": "2021-06-30T10:45:57.274432"}
        dictionary_2 = {"id": "64a8e9f5-4840-431c-9305-baff80edd779",
                        "created_at": "2021-06-30T10:45:57.274438",
                        "updated_at": "2021-06-30T10:45:57.274438"}
        instance_1 = BaseModel(**dictionary)
        self.storage.new(instance_1)
        instance_2 = BaseModel(**dictionary_2)
        self.storage.new(instance_2)
        self.storage.save()
        with open('file.json', 'r', encoding='utf-8') as myfile:
            file_content = json.load(myfile)
            self.assertTrue(
                "BaseModel.64a8e9f5-4840-431c-9305-baff80edd778",
                file_content.keys())
            self.assertTrue(
                "BaseModel.64a8e9f5-4840-431c-9305-baff80edd779",
                file_content.keys())

    def test_reload(self):
        '''Testing function to check the instance method reload'''
        with open('file.json', 'w', encoding='utf-8') as myfile:
            class_write = "{\"BaseModel.7c1ef07d-5b19-42a0-85d0-67b3ec96\": \
                            {\"id\": \"7c1ef07d-5b19-42a0-85d0-67b3ec96\", \
                            \"created_at\": \"2021-06-30T10: 51: 30.849940\", \
                            \"updated_at\": \"2021-06-30T10: 51: 30.849940\", \
                            \"__class__\": \"BaseModel\"}}"
            myfile.write(class_write)
            self.storage.reload()
            object = self.storage.all()
            self.assertTrue(
                "BaseModel.7c1ef07d-5b19-42a0-85d0-67b3ec96a50f",
                object.keys())

    def test_exceding_args(self):
        '''Testing function to check methods with more arguments'''
        dictionary = {"id": "64a8e9f5-4840-431c-9305-baff80edd778",
                      "created_at": "2021-06-30T10:45:57.274432",
                      "updated_at": "2021-06-30T10:45:57.274432"}
        test = BaseModel(**dictionary)
        with self.assertRaises(TypeError):
            self.storage.new(test, test)

        with self.assertRaises(TypeError):
            self.storage.save(test)

        with self.assertRaises(TypeError):
            self.storage.reload(test)
