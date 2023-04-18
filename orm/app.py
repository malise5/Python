# //List
pet_name = ["Rose", "Meow", "Dew", "kude", "Doggy", "harre"]

# print(pet_name[0])
# print(pet_name[2:6])
# print(pet_name.reverse())
# print(pet_name[0].upper())
# print(pet_name[0].title())
# pet_name.append("AStro")
# pet_name.insert(0, "kuku")
# pet_name.pop()
# print(pet_name)
# pet_name.clear()
# print(pet_name)

# TUPLES
# pet_age = (1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(pet_age.count(2))
# print(pet_age)

# for i in range(0, 10):
#     print(i)

# SETS
# pet_food = {"nyama", "kachumba", "liku", "liku"}
# print(pet_food)

# DICTIONAR
pet_info = {
    "name": "luku",
    "age": 5,
    "breed": "domestic long"
}
# pets = dict(name="kudez", age=25, breed="snko")
# print(pet_info["age"])
# print(pet_info.get("laugh", "Attribute not found"))

# FUNCTIONS


def pet_list(list):
    for pet in list:
        print(pet)


pet_list(pet_name)
