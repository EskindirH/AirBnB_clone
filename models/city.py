#!/usr/bin/python3

"""

Module contains city model

"""

from models.base_model import BaseModel


class City(BaseModel):
    """Defines city to look for"""
    state_id = ""
    name = ""
