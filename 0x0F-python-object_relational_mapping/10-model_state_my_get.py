#!/usr/bin/python3
"""
listing id of a given state
"""
import sqlalchemy
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == '__main__':
    # pass in arguments and connect to db
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = sys.argv[4]
    condition = [state]
    result = session.query(State.id) \
        .filter(State.name.in_(condition)) \
        .all()

    if result:
        for i in result:
            print(i[0])
    else:
        print("Not found")
