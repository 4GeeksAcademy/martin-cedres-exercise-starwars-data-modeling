import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    # Defino la columna de la tabla user
    # Cada columna también es un atributo de instancia normal de Python.
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    height = Column(String(50), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    climate = Column(String(100), nullable=False)
    


class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    chararcters_id = Column(Integer, ForeignKey('characters.id')) # Con Foreingkey establece el vinculo logico entre dos tablas 
    characters = relationship(Characters) # El relationship utiliza la relacion par afacilitar el acceso al codigo (obtiene los objetos de las tablas) 
    planets_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship(Planets)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
