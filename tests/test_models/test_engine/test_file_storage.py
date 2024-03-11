#!/usr/bin/python3
"""
Test for File Storage
This module contains unit tests for the FileStorage class
in the engine module
"""

import json
import unittest
import uuid
import pep8
import os
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class TestFileStorage(unittest.TestCase):
    """
    Unit tests for the FileStorage class in the engine module.
    """

    @classmethod
    def setUpClass(cls):
        """Set up for the test."""
        cls.user = User()
        cls.user.first_name = "Amin"
        cls.user.last_name = "si"
        cls.user.email = "gitthing@done.com"
        cls.storage = FileStorage()
        cls.path = "file.json"

    @classmethod
    def teardown(cls):
        """At the end of the test, this will tear it down."""
        del cls.user
        """ if deleting the file """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def tearDown(self):
        """tear down"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_FileStorage(self):
        """Test pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "Fix pep8")

    def test_docstring(self):
        """ Test docstring """
        self.assertIsNotNone(FileStorage.__doc__)

    def test_documentation(self):
        """ Test documentation, created and not empty """
        self.assertTrue(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertTrue(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertTrue(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertTrue(FileStorage.reload.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_all(self):
        """tests if everythingd works fine in the File Storage"""
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._FileStorage__objects)

    def test_new(self):
        """test if new is created"""
        storage = FileStorage()
        obj = storage.all()
        user = User()
        user.id = "667788"
        user.name = "amin"
        storage.new(user)
        key = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(obj[key])

    def test_reload_filestorage(self):
        """ tests reload """
        self.storage.save()
        Root = os.path.dirname(os.path.abspath("console.py"))
        path = os.path.join(Root, "objects.json")
        with open(path, 'r') as f:
            lines = f.readlines()
        try:
            os.remove(path)
        except Exception:
            pass
        self.storage.save()
        with open(path, 'r') as f:
            lines2 = f.readlines()
        self.assertEqual(lines, lines2)
        try:
            os.remove(path)
        except Exception:
            pass
        with open(path, "w") as f:
            f.write("{}")
        with open(path, "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(self.storage.reload(), None)

    def test_pep8_conformance_file_storage(self):
        """Test for PEP8 compliance"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
