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

    def print_cat_details(self):
        super().print_pet_details()
        print(f'''
            Indoor: {self.indoor}
        ''')


ipdb.set_trace()
