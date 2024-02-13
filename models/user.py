#!/usr/bin/python3

"""

This module contains User model class

"""


from models.base_model import BaseModel


class User(BaseModel):
    """User model class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
