#!/usr/bin/python3
"""
City relationship
"""
import sqlalchemy
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    # connect to db and create state n city
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)
    # creating a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Creating State "California
    cali = State(name="California")

    # Creating a city and linking it to state
    san = City(name="San Francisco")
    cali.cities.append(san)

    # adding both State and City to the session
    session.add(cali)

    session.commit()
    # Closing the connection

    session.close()
