import os
from typing import Final
from dotenv import load_dotenv
import psycopg
from psycopg.rows import dict_row

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_PORT = os.getenv('DATABASE_PORT', '5432')  # Provide default port 5432
DATABASE_NAME = os.getenv('DATABASE_NAME')

connection_string = (
    f"dbname={DATABASE_NAME} user={DATABASE_USERNAME} password={DATABASE_PASSWORD} host={DATABASE_HOST}"
    f" port={DATABASE_PORT}")

CREATE_CHARACTERS_TABLE = """
CREATE TABLE IF NOT EXISTS characters (
    user_id VARCHAR(50),
    username VARCHAR(50),
    char_name VARCHAR(50),
    stats JSONB
);
"""


def databaseCONN():
    try:
        connection = psycopg.connect(connection_string)
        cursor = connection.cursor()
        cursor.execute(CREATE_CHARACTERS_TABLE)
        connection.commit()
        cursor.close()
        print("Connection to PostgreSQL DB successful and table ensured.")
        return connection
    except Exception as error:
        print(f"Error while connecting to PostgreSQL: {error}")
        return None


class Oauth:
    def __init__(self):
        self.token = TOKEN
        self.OWNER_IDS = ['627569347417866271']

    def discordTOKEN(self):
        return self.token, self.OWNER_IDS
