#!/usr/bin/python3
"""
Model definition
"""
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table


Base = declarative_base()


class State(Base):
    """
    my model definition
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=True, autoincrement=True)
    name = Column(String(128), nullable=False)