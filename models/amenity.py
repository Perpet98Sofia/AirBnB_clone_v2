#!/usr/bin/python3
""" instances amenities """
from models.base_model import BaseModel, Base
from models.city import City
from models.user import User
from models.place import place_amenity
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from os import environSTORAGE = getenv("HBNB_TYPE_STORAGE")


class Amenity(BaseModel, Base):
    """Permit to add the amenities for places"""
    __tablename__ = "amenities"
    if STORAGE == "db":
        name = Column(String(128), nullable=False)
        place_amenities = relationship(
            'Place', secondary=place_amenity, back_populates="amenities")

    else:
        name = ""
