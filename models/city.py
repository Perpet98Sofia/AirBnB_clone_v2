#!/usr/bin/python3
"""This is the city class."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from models.state import State
from sqlalchemy.orm import relationship
from os import environ

STORAGE = getenv("HBNB_TYPE_STORAGE")


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    
    if STORAGE == "db":
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship('Place',
                              backref='cities',
                              cascade="all, delete-orphan")
    else:
        name = ""
        state_id = ""
