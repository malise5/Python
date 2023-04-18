import ipdb
import sqlite3

CONN = sqlite3.Connection('./data.db')

CURSOR = CONN.cursor()


class Pet:

    total_pets = 0

    def __init__(self, name, species, breed, temperament, id=None):
        self.name = name
        self.species = species
        self.breed = breed
        self.temperament = temperament
        self.id = id

        Pet.increase_pets()

    def print_pet(self):
        print(self)

    def print_pet_details(self):
        print(f"""
            name: {self.name}, 
            age: {self.age}, 
            breed: {self.breed}, 
            temperament: {self.temperament},
            owner: {self.owner}
        """)

    # CLASS METHOD
    @classmethod
    def increase_pets(cls):
        cls.total_pets += 1
        print(f"one new pet added")
