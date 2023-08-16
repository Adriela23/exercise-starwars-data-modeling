import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class planet(Base):
    __tablename__ = 'planets'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    population = Column(String(15))
    terrain = Column(String(50))
    surface_water = Column(Integer)
    climate = Column(String(50))


class vehicle(Base):
    __tablename__ = 'vehicles'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    model = Column(String(20))
    vehicle_class = Column(String(20))
    cost_in_credits = Column(String(15))
    max_atmosphering_speed = Column(Integer)
    length = Column(Integer)
    passengers = Column(Integer)


class character(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    birth_year = Column(String(20))
    height = Column(Integer)
    mass = Column(Integer)
    gender = Column(String(20))

    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(planet)
    
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    vehicle = relationship(vehicle)


class user(Base):
    __tablename__= 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    username = Column(String(20), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(20), nullable=False)


class fav_character(Base):
    __tablename__= 'fav_characters'

    id = Column(Integer, primary_key=True)

    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(character)

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(user)


class fav_planet(Base):
    __tablename__= 'fav_planets'

    id = Column(Integer, primary_key=True)

    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(planet)

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(user)


class fav_vehicle(Base):
    __tablename__= 'fav_vehicles'

    id = Column(Integer, primary_key=True)

    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    vehicle = relationship(vehicle)

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(user)




    def to_dict(self):
        return {}


# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
