#!/usr/bin/python3
""" This module houses the basemodel class """


from uuid import uuid4
from datetime import datetime, date, time, timezone


class BaseModel():
    """ Base model class """

    def __init__(self, *args, **kwargs):
        """ Init method """
        if 'created_at' in kwargs:
            created = kwargs['created_at']
            self.created_at = datetime.fromisoformat(created)
        else:
            self.created_at = datetime.now().isoformat()
        if 'updated_at' in kwargs:
            updated = kwargs['updated_at']
            self.updated_at = datetime.fromisoformat(updated)
        else:
            self.updated_at = datetime.now().isoformat()
        if 'id' in kwargs:
            self.id = kwargs['id']
        else:
            self.id = uuid4()
        if 'my_number' in kwargs:
            self.my_number = kwargs['my_number']
        if 'name' in kwargs:
            self.name = kwargs['name']

    def __str__(self):
        """ Override __str__ method """
        myid = self.id
        mydict = self.__dict__
        return ("[{}] ({}) {}".format(__class__.__name__, myid, mydict))

    def save(self):
        """ Method updates the updated_at attribute """
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        """ Method returns a dictionary containing all keys/values of __dict__
        of the instance """
        self.__dict__['__class__'] = __class__.__name__
        return self.__dict__
