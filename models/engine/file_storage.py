#!/usr/bin/python3

"""
File Storage Module
This module handles the storage of classes and their management.
"""

import json
from os import path
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """
    File Storage Class
    This class represents the file storage module.
    Attributes:
        __file_path (str): The path of the JSON file where the
        contents of the `__objects` variable will be stored.
        __objects (dict): Stores all the instances' data.
    """
    __file_path = 'objects.json'
    __objects = {}

    def all(self):
        """
        Get objects information
        Returns the content of the `__objects` class attribute.
        """
        return self.__objects

    def new(self, obj):
        """
        Save a New Object
        Args:
            obj (inst): The object to add to the `__objects`
            class attribute.

        Sets in the `__objects` class attribute the instance data
        with a key as <obj class name>.id.
        """
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        Serialize `__objects` Content
        Serializes the content of the `__objects` class attribute
        to the path specified in the `__file_path` class attribute
        in JSON format, with the `created_at` and
        `updated_at` formatted.
        """
        json_dict = {}
        for k, v in self.__objects.items():
            json_dict[k] = v.to_dict()
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            f.write(json.dumps(json_dict))

    def reload(self):
        """
        Deserialize JSON File
        If the file specified in the `__file_path` class attribute exists,
        each object in the file will be deserialized and appended to the
        `__objects` class attribute as an instance with the object data.
        """
        if path.exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                json_dict = json.loads(f.read())
                for k, v in json_dict.items():
                    self.__objects[k] = eval(v['__class__'])(**v)
