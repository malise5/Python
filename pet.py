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

    # Creating table
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

    # dROPPING THE TABLE
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
        # self.id = CURSOR.lastrowid

        CURSOR.execute(sql, (self.name, self.species,
                       self.breed, self.temperament))

    @classmethod
    def create(cls, name, species, breed, temperament):
        # __init__(cls, name, species, breed,
        pet = cls(name, species, breed, temperament)

        # persist New Instance to database
        pet.save()

        return pet

    @classmethod
    def get_newest_pet(cls, row):
        pet = cls(
            id=row[0],
            name=row[1],
            species=row[2],
            breed=row[3],
            temperament=row[4],
        )
        return pet

    @classmethod
    def get_all(cls):
        sql = '''
            SELECT * FROM pets
        '''

        return [cls.get_newest_pet(row) for row in CURSOR.execute(sql)]

    @classmethod
    def find_by_name(cls, name):
        sql = '''
            SELECT * FROM pets
            WHERE name = ?
            LIMIT 1
        '''
        row = CURSOR.execute(sql, (name)).fetchone()
        if not row:
            return None
        else:
            cls(
                id=row[0],
                name=row[1],
                species=row[2],
                breed=row[3],
                temperament=row[4],
            )
