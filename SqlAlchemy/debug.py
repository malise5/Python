
import ipdb

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import (Base, Pet)

if __name__ == '__main__':
    # creating Engine
    engine = create_engine('sqlite:///pet_app.db')
    Base.metadata.create_all(engine)

    # creating session
    Session = sessionmaker(bind=engine)
    session = Session()

    # creating a pet and seve it to the database with 'session.add() and session.commit()'
    rose = Pet(name='rose', species='cat', breed='domestic longhair',
               temperament='relaxed', owner_id=1)
    spot = Pet(name='spot', species='dog', breed='husky',
               temperament='joyful', owner_id=2)

    # PERSSISTING INDIVIDUAL INSTANCE TO DB
    # session.add(rose)
    # session.commit()

    # PERSSISTING MULTIPLE INSTANCE TO DB
    session.bulk_save_objects([rose, spot])
    session.commit()

    # Resources ALL INSTANCES
    pets = session.query(Pet)

    # print the pets
    print([pet for pet in pets])


ipdb.set_trace()
