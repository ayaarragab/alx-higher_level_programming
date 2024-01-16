#!/usr/bin/python3
"""
a script 14-model_city_fetch_by_state.py
that prints all City objects from
the database hbtn_0e_14_usa
"""
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

from sys import argv

from model_city import City
from model_state import State

if __name__ == '__main__':
    engine_str = f'mysql://{argv[1]}:{argv[2]}' + \
                 f'mysql://{argv[1]}:{argv[2]}@' + \
                 f'localhost:3306/{argv[3]}'
    engine = create_engine(engine_str)
    Session = sessionmaker(bind=engine)
    session = Session()
    cityQ = session.query(City).order_by(City.id).all()
    stateQ = session.query(State).order_by(State.id).all()
    for row1 in stateQ:
        for row2 in cityQ:
            if row1.id == row2.state_id:
                print(f"{row1.name}: ({row2.id}) {row2.name}")
    session.close()
