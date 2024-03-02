#!/usr/bin/python3
"""create a unique FileStorage instance for your application
"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


from os import environ

dummy_classes = {"BaseModel": BaseModel, "User": User,
                 "Review": Review, "City": City,
                 "State": State, "Place": Place,
                 "Amenity": Amenity}

dummy_tables = {"states": State, "cities": City,
                "users": User, "places": Place,
                "reviews": Review, "amenities": Amenity}

storage_engine = environ.get("HBNB_TYPE_STORAGE")

if (storage_engine == "db"):
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
