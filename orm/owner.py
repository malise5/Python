import ipdb
import sqlite3


CONN = sqlite3.Connection('./data.db')

CURSOR = CONN.cursor()


class Owner:
    def __init__(self, age):
        self.age = age

    def get_name(self):
        print(self.name)

    def set_name(self, name):
        if (type(name) == str):
            self._name = name
        else:
            print("Name must be a string!!")

    name = property(get_name, set_name)
