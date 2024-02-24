import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from datetime import datetime
from eralchemy2 import render_er


Base = declarative_base()

# Tabla de asociación para la relación de muchos a muchos entre usuarios y planetsas
favorite_planets_association = Table('favorite_planets', Base.metadata,
    Column('users_id', ForeignKey('users.id'), primary_key=True),
    Column('planets_id', ForeignKey('planets.id'), primary_key=True)
)

# Tabla de asociación para la relación de muchos a muchos entre usuarios y personajes
favorite_characters_association = Table('favorite_characters', Base.metadata,
    Column('users_id', ForeignKey('users.id'), primary_key=True),
    Column('characters_id', ForeignKey('characters.id'), primary_key=True)
)

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)
    subscription_date = Column(DateTime, default=datetime.utcnow)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    # Relaciones
    favorite_planets = relationship('planets', secondary=favorite_planets_association)
    favorite_characters = relationship('characters', secondary=favorite_characters_association)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    # Relación inversa para los favoritos
    favorited_by = relationship('users', secondary=favorite_planets_association)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    # Relación inversa para los favoritos
    favorited_by = relationship('users', secondary=favorite_characters_association)

class Posts(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    content = Column(String(1000), nullable=False)
    published_date = Column(DateTime, default=datetime.utcnow)
    author_id = Column(Integer, ForeignKey('users.id'))
    author = relationship('users')


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
