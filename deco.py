import ipdb

# CALLBACK FUNCTION


def walk(pet):
    print(f"{pet} walked")


def feed(pet):
    print(f"{pet} fed")

# HIGHER ORDER FUNCTIONS


def higher_order():
    def inner():
        print("Hallow from inner")
    return inner


ipdb.set_trace()
