#!/usr/bin/python3
"""
a script that prints the first
State object from the database hbtn_0e_6_usa
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
    # Object that its role to make a session
    session = Session()
    myQuery = session.query(State)
    for row in myQuery.filter(State.name.like('%a%')).order_by(State.id).all():
        print(f'{row.id}: {row.name}')
    session.close()
