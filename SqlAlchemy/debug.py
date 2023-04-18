from pet import Pet, CONN, CURSOR
from owner import Owner, CONN, CURSOR
# from cat import Cat
import ipdb

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import (Base, Pet)

if __name__ == '__main__':
    
