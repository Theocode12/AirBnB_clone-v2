#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base, Relationship
from sqlalchemy import (
    Column,
    String,
)
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")

class Amenity(BaseModel, Base):
    """ Amenity class to store amenity information """
    if storage_type == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
    else:
        name = ""
