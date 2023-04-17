import ipdb


class Pet:

    total_pets = 0

    def __init__(self, name, age, breed, temperament, owner="No Owner"):
        self.name = name
        self.age = age
        self.breed = breed
        self.temperament = temperament
        self.owner = owner

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
