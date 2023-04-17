import ipdb


class Pet:
    def __init__(self, name, age, breed, temperament, owner="No Owner"):
        self.name = name
        self.age = age
        self.breed = breed
        self.temperament = temperament
        self.owner = owner

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
