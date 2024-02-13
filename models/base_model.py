#!usr/bin/python3
"""
Module containing parent class
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Class defining common attribs/methonds
    """
    def __init__(self, *args, **kwargs):
        """Initializes instances

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            void
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
        else:
             f = "%Y-%m-%dT%H:%M:%S.%f"
             for key, value in kwargs.items():
                 if key == 'created_at' or key == 'updated_at':
                     value = datetime.strptime(kwargs[key], f)
                 if key != '__class__':
                     setattr(self, key, value)

    def __str__(self):
        """Returns string representation

        Returns:
            string representation
        """
        class_name = "[" + self.__class__.__name__ + "]"
        dct = {k: v for (k, v) in self.__dict__.items() if (not v) is False}
        return class_name + " (" + self.id + ") " + str(dct)

    def save(self):
        """Updates last update time
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values

        Returns:
            dictionary containg key/value
        """
        new_dict = {}
        
        for key, value in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                new_dict[key] = value.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                new_dict[key] = value
        new_dict['__class__'] = self.__class__.__name__

        return new_dict

