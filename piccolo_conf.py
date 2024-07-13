
from piccolo.engine.postgres import PostgresEngine


DB = PostgresEngine(config={
    'host': 'localhost',
    'database': 'dnd',
    'user': 'postgres',
    'password': 'password'
})

