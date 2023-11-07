#!/usr/bin/python3
'''a class BaseModel that defines all common
attributes/methods for other classes'''

import uuid
import datetime


class BaseModel:
    '''Base Class

    Attributes:
        id: string - assign with an uuid when an instance is created
        created_at: datetime - assign with the current datetime when
        an instance is created
        updated_at: datetime - assign with the current datetime when
        an instance is updated
    '''

    def __init__(self, *args, **kwargs):
        '''Startup function'''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        '''String Presentation'''
        return (f'[{type(self).__name__}] ({self.id}) {str(self.__dict__)}')

    def save(self):
        '''updates the public instance attribute updated_at with
        the current datetime'''
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        '''returns a dictionary containing all keys/values
        of __dict__ of the instance'''
        new_dict = self.__dict__
        new_dict['__class__'] = type(self).__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
