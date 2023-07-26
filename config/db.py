from config.static_configs import StaticConfigs
from sqlalchemy import create_engine

class PostgresConnect:
    def __init__(self):
        self.engine = create_engine(StaticConfigs.DATABASE_URI, isolation_level="AUTOCOMMIT")