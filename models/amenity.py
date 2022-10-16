#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base, Relationship
from sqlalchemy import (
    Column,
    String,
)
from os import getenv


class Amenity(BaseModel, Base):
    """ Amenity class to store amenity information """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
