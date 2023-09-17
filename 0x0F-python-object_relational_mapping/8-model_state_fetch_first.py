#!/usr/bin/python3

"""
Script that prints the first State object from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    # create an engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    # create a configured class Session
    Session = sessionmaker(bind=engine)
    # create a Session instance
    session = Session()
    # query to get the first State object
    state = session.query(State).first()
    # print the id and name of the first State object
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
    # close session to end the program
    session.close()
