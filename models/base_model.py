#!/usr/bin/python3

"""Base_Model Module:

This module defines the Base Model,
a reference for other classes
in the HBNB project (Airbnb Clone).
It includes a universally unique identifier,
creation and update timestamps, a standard
representation format, and methods for
data serialization and deserialization.
"""

from datetime import datetime
import models
import uuid


class BaseModel:
    """ Base Model class:
    manages the initialization, serialization, and deserialization 
    of instances.
    Attributes:
        id (str): A universally unique identifier for each instance.
        created_at (datetime): The timestamp when an instance is created.
        updated_at (datetime): Ths timestamp of the last update.
    """

    def __init__(self, *args, **kwargs):
        """
        Base Model Initialization:
        Initializes default values for a Base Model instance.
        """
        if kwargs:
            for arg, val in kwargs.items():
                if arg in ('created_at', 'updated_at'):
                    val = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')

                if arg != '__class__':
                    setattr(self, arg, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """
        String Representation:
        Returns a string with the class name, instance ID,
        and dictionary representation.
        """
        return '[{0}] ({1}) {2}'.format(
                self.__class__.__name__, self.id, self.__dict__
            )

    def save(self):
        """
        Update and Save:
        Updates the instance's `updated_at` attribute
        and saves the class data to a file.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Convert to Dictionary:
        Converts the instance information to a dictionary
        for human-readable format.
        """
        class_info = self.__dict__.copy()
        class_info['__class__'] = self.__class__.__name__
        class_info['created_at'] = self.created_at.isoformat()
        class_info['updated_at'] = self.updated_at.isoformat()

        return class_info
