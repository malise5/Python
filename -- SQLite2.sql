-- SQLite

--owner table
CREATE TABLE owners(
    id INTEGER PRIMARY KEY,
    name STRING,
    address STRING,
    email STRING,
    phone INTEGER
);

--Pet table
CREATE TABLE pets(
    id INTEGER PRIMARY KEY,
    name STRING,
    age INTEGER,
    breed STRING,
    birthdate INTEGER,
    favorite_treats TEXT,
    last_fed_at DATETIME,
    last_walked_at DATETIME,
    owner_id INTEGER,
        FOREIGN KEY (owner_id) REFERENCES owner (id)
);

ALTER TABLE pets 
ADD COLUMN image_url TEXT;

--SEEDING TABLE FOR OWERS
INSERT INTO owners(name, address, email, phone) VALUES("kudz", "99 8th st seattle", "kudezx@gmail.com", 0703750755);

INSERT INTO owners(name, address, email, phone) VALUES("malise", "moyale butiye", "malise@gmail.com", 0703560755);

--SEEDING TABLE FOR OWERS
INSERT INTO pets(name, age, breed,birthdate,favorite_treats, last_fed_at, last_walked_at, owner_id, image_url) VALUES("rose", 2, "shiba inu", 2021, "crackers", "2023-01-04", "2023-22-04", 1, "https://images.indianexpress.com/2021/06/Puppy-Pixabay.jpg");

INSERT INTO pets(name, age, breed,birthdate,favorite_treats, last_fed_at, last_walked_at, owner_id, image_url) VALUES("luku", 5, "shiba inu", 2008, "crackers", "2023-01-04", "2023-22-04", 2, "https://images.indianexpress.com/2021/06/Puppy-Pixabay.jpg");

--//CRUD ACTIONS
--API Endpoints --
SELECT * FROM pets;

SELECT * FROM pets
WHERE name = "luku",

UPDATE pets SET age = 10 WHERE name = "rose";

SELECT pets.name, owners.name as "owners" FROM pets JOIN owners ON pets.owner_id = owners.id