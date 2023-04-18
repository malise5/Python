from sqlalchemy import (PrimaryKeyConstraint, Column, String, Integer)

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# class Pet inherit the base class


class Pet(Base):
    # creating pets table
    __tablename__ = 'pet'

    # adding arguuments for primary id to pet table
    __table_args__ = (PrimaryKeyConstraint('id'),)

    # creating columns of the pet table
    id = Column(Integer())
    name = Column(String())
    species = Column(String())
    breed = Column(String())
    temperament = Column(String())
    owner_id = Column(Integer())

    # returns all the columns of the pet table
    def __repr__(self):
        return f"ID: {self.id},"\
            + f"Name: {self.name},"\
            + f"Species: {self.species},"\
            + f"Breed: {self.breed},"\
            + f"Temperament: {self.temperament},"\
            + f"Owner_ID: {self.owner_id}"
    # after abover record we migrate using "alembic init migration"
    # inside the alembic.ini in the migration we set it to sqlalchemy.url = sqlite://pet_app.db
