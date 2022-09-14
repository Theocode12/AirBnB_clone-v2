#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base, Relationship
import models
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import (
    Column,
    Integer,
    String,
    FLOAT,
    Table,
    ForeignKey
)
metadata = Base.metadata


class Place(BaseModel, Base):
    """ A place to stay """
    if models.storage_type == "db":
        __tablename__ = "places"
        city_id = Column(String(128), nullable=False)
        user_id = Column(String(128), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(128), nullable=False)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(FLOAT(precision=10, scale=2), nullable=True)
        longitude = Column(FLOAT(precision=10, scale=2), nullable=True)
        amenities = Relationship(
            "Amenity", secondary="place_amenity",
            backref="place_amenity", viewonly=False
        )
        reviews = Relationship(
            "Review", cascade="all, delete", backref="place_amenity")
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    if models.storage_type == "db":
        place_amenity = Table(
            "place_amenity",
            metadata,
            Column(
                "place_id", String(60), ForeignKey("places.id"),
                primary_key=True, nullable=False),
            Column(
                "amenity_id", String(60), ForeignKey("amenities.id"),
                primary_key=True, nullable=False),
        )
    else:
        @property
        def amenities(self):
            # Please crosscheck this getter
            """
            Getter attribute amenities
            that returns the list of Amenity instances
            """
            amenity_ids = []
            amenities = models.storage.all(Amenity)
            for amenity in amenities.values():
                if amenity.place_id == self.id:
                    amenity_ids.append(amenity)
            return amenity_ids

        @amenities.setter
        def amenities(self):
            # Please crosscheck this setter
            """
            Setter attribute amenities
            that returns the list of Amenity instances
            """
            result = []
            amenities = models.storage.all(Amenity)
            for amenity in amenities.values():
                if amenity.id == self.id:
                    result.append(amenity)
            self.amenity_ids = result
