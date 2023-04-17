import ipdb
from pet import Pet


class Cat(Pet):
    def __init__(self, name, age, breed, temperament, indoor):
        # self.name = name
        # self.age = age
        # self.breed = breed
        # self.temperament = temperament
        super().__init__(name, age, breed, temperament)
        self.indoor = indoor

    def talk(self):
        print(f"{self.name} say Hallo")


ipdb.set_trace()
