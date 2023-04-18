import ipdb
import sqlite3

CONN = sqlite3.Connection('./data.db')

CURSOR = CONN.cursor()


class Pet:

    def __init__(self, name, species, breed, temperament, id=None):
        self.id = id
        self.name = name
        self.species = species
        self.breed = breed
        self.temperament = temperament

    @classmethod
    def create_table(cls):
        sql = '''
            CREATE TABLE IF NOT EXISTS pets
                (id INTEGER PRIMARY KEY,
                name STRING,
                species STRING,
                breed STRING,
                temperament STRING
                );
        '''

        CURSOR.execute(sql)

    @classmethod
    def drop_table(cls):
        sql = '''
            DROP TABLE IF EXISTS pets
        '''
        CURSOR.execute(sql)

    def save(self):
        sql = '''
            INSERT INTO pets(name, species, breed, temperament)
            VALUES (?,?,?,?)
        '''
        CURSOR.execute(sql, (self.name, self.species,
                       self.breed, self.temperament))
        self.id = CURSOR.lastrowid
