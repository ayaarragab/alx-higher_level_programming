#!/usr/bin/python3
"""
a script that adds the State
object “Louisiana” to the database
hbtn_0e_6_usa
"""
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

from sys import argv

from model_state import State, Base

if __name__ == '__main__':
    engine_str = f'mysql://{argv[1]}:{argv[2]}' + \
                 f'mysql://{argv[1]}:{argv[2]}@' + \
                 f'localhost:3306/{argv[3]}'
    engine = create_engine(engine_str)
    Session = sessionmaker(bind=engine)
    session = Session()
    newState = State()
    newState.name = 'Louisiana'
    session.add(newState)
    session.commit()
    print(newState.id)
    session.close()
