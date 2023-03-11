#!/usr/bin/python3
"""Module houses our FileStorage class"""


class FileStorage:
    """This is a class that will serialize instances to a JSON
    files and deserialize JSON files to instances"""

    __objects = {}

    def __init__(self):
        self.__objects = {"__class__.__name__":self.id}
    def all(self):
        return self.__objects
    
    def new(self, obj):
        __objects = {

