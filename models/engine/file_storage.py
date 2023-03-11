#!/usr/bin/python3
"""Module houses our FileStorage class"""


class FileStorage:
    """This is a class that will serialize instances to a JSON
    files and deserialize JSON files to instances"""

    __objects = {}
    __file_path = "file.json"

    """def __init__(self):
        init method
        self.__objects = {"__class__.__name__":self.id}
    """
    def all(self):
        """Returns the dictionary named __objects"""
        return self.__objects

    def new(self, obj):
        """Sets __objects the obj with key <obj class name>.id"""
        __objects = {obj.__class__.__name__: obj.id}

    def reload(self):
        """Deserializes the JSON file to __objects only if the JSON file
        exists; otherwise, do nothing and do not raise an exception"""
        pass
