from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Pet, Owner

if __name__ == '__main__':
    engine = create_engine('sqlite:///pet_app.db')
    Session = sessionmaker(bind=engine)
    session = Session()

# 2.a 🌲 add delete methods for Pet and Owner
    session.query(Pet).delete()
    session.query(Owner).delete()

# Initialize Faker
    faker = Faker()

# list of species Cat and Dog
    species = ["Cat", "Dog"]

# cat breeds
    cat_breeds = ["Domestic Long hair", "Female Long hair",
                  "Domestic Long hair", "Siamse", "Ragdoll", "Sphynx"]

# dog breeds
    dog_breeds = ["Mix", "Husky", "Malamute",
                  "Dachshound", "Samoyed", "Shiba Inu", "Corgi"]

# Temparment list
    temparament = ["Calm", "Nervous", "Mischevious", "Aggressive", "Hyper"]

# Owners
    owners = []

    for _ in range(50):
        owner = Owner(
            name=f"{faker.first_name()} {faker.last_name}",
            email=faker.email(),
            phone=random.randint(1000000000, 9999999999),
            address=faker.address(),
        )

    session.add(owner)
    session.commit()
# append new owner to owners array
    owners.append(owner)
