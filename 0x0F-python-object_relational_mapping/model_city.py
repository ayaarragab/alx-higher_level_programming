#!/usr/bin/python3
"""Start link class to table in database
"""
import sys

from model_state import Base, State

from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """
    City class
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
