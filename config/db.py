DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@db:5432/bitespeed'
from sqlalchemy import create_engine

class PostgresConnect:
    def __init__(self):
        self.engine = create_engine(DATABASE_URI)