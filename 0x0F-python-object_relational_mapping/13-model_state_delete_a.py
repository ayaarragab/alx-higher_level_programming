#!/usr/bin/python3
"""
a script that changes the name of
a State object from the database
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
    myQuery = session.query(State)
    allHaveA = myQuery.filter(State.name.like('%a%')).order_by(State.id).all()
    for row in allHaveA:
        session.delete(row)
    session.commit()
    session.close()
