from sqlalchemy import (PrimaryKeyConstraint, Column,
                        String, Integer, Float, Boolean, DateTime, ForeignKey)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

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
    # 1 🌲 add ForeignKey
    owner_id = Column(Integer(), ForeignKey('owners.id'))

    # returns all the columns of the pet table

    def __repr__(self):
        return f"ID: {self.id},"\
            + f"Name: {self.name},"\
            + f"Species: {self.species},"\
            + f"Breed: {self.breed},"\
            + f"Temperament: {self.temperament},"
    # after abover record we migrate using "alembic init migration"
    # inside the alembic.ini in the migration we set it to sqlalchemy.url = sqlite://pet_app.db


class Owner(Base):
    __tablename__ = 'owners'
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    email = Column(String())
    phone = Column(Integer())
    address = Column(String())

    # Asscociate the Pet Model with Owner Model
    # relationship('Pet', backref=backref('pet))
    pets = relationship('Pet', backref=backref('pet'))

    # returns all the columns of the Owner table
    def __repr__(self):
        return f"ID: {self.id},"\
            + f"Name: {self.name},"\
            + f"Email: {self.email},"\
            + f"Phone: {self.phone},"\
            + f"Address: {self.address},"
    # after abover record we migrate using "alembic init migration"
    # inside the alembic.ini in the migration we set it to sqlalchemy.url = sqlite://pet_app.db
    # alembic upgrade head
