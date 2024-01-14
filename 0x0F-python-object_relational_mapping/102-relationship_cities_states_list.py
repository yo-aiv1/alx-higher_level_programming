#!/usr/bin/python3
"""Fetch all data in citites table."""

if __name__ == "__main__":
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    data = session.query(State).join(City).order_by(City.id).all()

    for state in data:
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))
