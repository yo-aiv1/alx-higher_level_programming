#!/usr/bin/python3
"""Fetch all data in citites table."""

if __name__ == "__main__":
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    data = session.query(State, City).filter(State.id == City.state_id).all()

    for state, city in data:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
