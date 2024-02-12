#!usr/bin/python3
"""
Module containing storage logic
"""

import os
import json

class FileStorage:
    """Serialize and deserialize JSON Object
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets __objects the obj with key <obj class name>.id"""
        key =  obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes objects"""
        dictionary = {}

        for k, v in FileStorage.__objects.items():
            dictionary[k] = v.to_dict()

        with open(FileStorage.__file_path, 'w') as f:
            json.dump(dictionary, f)

    def reload(self):
        """Deserializes objects from json file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.amenity import Amenity
        from models.state import State
        from models.review import Review
        from models.city import City

        dct = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'City': City, 'Amenity': Amenity, 'State': State,
               'Review': Review}
        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'w') as f:
                for k, v in json.load(f).items():
                    self.new(dct[v['__class__']](**v))
