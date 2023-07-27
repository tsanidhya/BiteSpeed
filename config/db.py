from config.static_configs import StaticConfigs
from sqlalchemy import create_engine
from sqlalchemy import text

class PostgresConnect:
    def __init__(self):
        self.engine = create_engine(StaticConfigs.DATABASE_URI, isolation_level="AUTOCOMMIT")
        with self.engine.connect() as con:
            with open("db_init.sql") as file:
                query = text(file.read())
                con.execute(query)
