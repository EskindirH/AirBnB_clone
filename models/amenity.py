#!/usr/bin/python3

"""

This module contains amenity model

"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """Defines amenities that user can choose
    from to offer at its place"""

    name = ""
