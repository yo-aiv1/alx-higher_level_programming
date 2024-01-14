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

    fetch = session.query(State).outerjoin(City).order_by(State.id, City.id)
    data = fetch.all()

    for state in data:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
           print("    {}: {}".format(city.id, city.name))
