#!/usr/bin/python3
"""
    Testing file for the class FileStorage
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()

    def test_save(self):
        '''Testing function to check the instance method save'''
        self.assertEqual(self.storage.save(), None)
