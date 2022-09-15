#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
import models
from sqlalchemy import (
    Column,
    String,
    ForeignKey
)
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")

class Review(BaseModel, Base):
    """ Review class to store review information """
    if storage_type == "db":
        __tablename__ = "reviews"
        text = Column(String(1024), nullable=False)
        place_id = Column(
            String(60), ForeignKey('places.id'),
            nullable=False)
        user_id = Column(
            String(60), ForeignKey('users.id'),
            nullable=False, )
    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """initializes Place"""
        super().__init__(*args, **kwargs)
