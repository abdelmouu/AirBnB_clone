#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Review Module

Inherits from BaseModel class.
Contains the attributes to be assigned
to the reviews created by the users.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review Class

    Attributes:
        place_id (str): The Place the Review belongs to
        user_id (str): The User that made the review
        text (str): The message the User wrote about the Place

    """
    place_id = ''
    user_id = ''
    text = ''
