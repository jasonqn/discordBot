import os
import asyncpg
from dotenv import load_dotenv

load_dotenv()

DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_PORT = os.getenv('DATABASE_PORT', '5432')
DATABASE_NAME = os.getenv('DATABASE_NAME')


async def create_db_pool():
    return await asyncpg.create_pool(
        user=DATABASE_USERNAME,
        password=DATABASE_PASSWORD,
        host=DATABASE_HOST,
        port=DATABASE_PORT,
        database=DATABASE_NAME
    )


class CreateUsers:
    CREATE_TABLE_USERS = """
        CREATE TABLE IF NOT EXISTS users(
        user_id BIGSERIAL PRIMARY KEY NOT NULL,
        username VARCHAR(255) NOT NULL
        );
        """

    INSERT_USER = """
    INSERT INTO users (username, user_id) 
    VALUES (%s, %s) 
    RETURNING id;
    """


class CreateCharacters:
    CREATE_TABLE_CHARACTERS = """
       CREATE TABLE IF NOT EXISTS characters (
           user_id VARCHAR(255) PRIMARY KEY,
           username VARCHAR(255) NOT NULL,
           char_name VARCHAR(255) NOT NULL,
           strength INTEGER NOT NULL,
           dexterity INTEGER NOT NULL,
           constitution INTEGER NOT NULL,
           intelligence INTEGER NOT NULL,
           wisdom INTEGER NOT NULL,
           charisma INTEGER NOT NULL
       );
       """

    INSERT_CHARACTER = """
       INSERT INTO characters (user_id, username, char_name, strength, dexterity, constitution, intelligence, wisdom, charisma)
       VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9)
       ON CONFLICT (user_id) DO NOTHING;
       """


INSERT_EVENT = "INSERT INTO events (user_id, event_name, dice_roll) VALUES (%s, %s, %s) RETURNING id;"
CHECK_USER = "SELECT * FROM users WHERE user_id = %s;"
INSERT_CHARACTER = "INSERT INTO characters (user_id, username, char_name, stats) VALUES (%s, %s, %s, %s);"
