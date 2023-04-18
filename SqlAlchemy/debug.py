
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

    # 3.1 ⌛ Create information
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

    # 3.2⌛ Read information
    # Resources ALL INSTANCES
    pets = session.query(Pet)

    # print the pets
    print([pet for pet in pets])

    # filter pet by temparament
    query_result = session.query(Pet).filter(Pet.temparament.like('%relaxed%'))

    for record in query_result:
        print(record)

    # 3.3 ⌛ Update information
    first_pet = session.query(Pet).first()
    first_pet.name = "Bud"
    session.commit()

    session.query(Pet).update({Pet.temparament: "Annoying"})
    pets = session.query(Pet)
    print([pet for pet in pets])

    # 3.4 ⌛ Delete the first information
    first_pet = session.query(Pet).first()
    session.delete(first_pet)
    pets = session.query(Pet)
    print([pet for pet in pets])

    # 3.4 ⌛ Delete the all information


ipdb.set_trace()
