#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""City Module
Inherits from BaseModel class.
Contains the attributes to be assigned
to the cities.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """City Class

    This is the City Class ...

    Attributes:
        state_id (str): The UUID of the State the City belongs to
        name (str): The City name

    """
    state_id = ''
    name = ''
