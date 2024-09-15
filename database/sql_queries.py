import os
import asyncpg
from dotenv import load_dotenv

load_dotenv()

DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_PORT = os.getenv('DATABASE_PORT')
DATABASE_NAME = os.getenv('DATABASE_NAME')


async def create_db_pool():
    connection = await asyncpg.create_pool(
        user=DATABASE_USERNAME,
        password=DATABASE_PASSWORD,
        host=DATABASE_HOST,
        port=DATABASE_PORT,
        database=DATABASE_NAME
    )
    print("Connection pool created successfully. DADDY")
    return connection


class CreateUsers:
    CREATE_TABLE_USERS = """
        CREATE TABLE IF NOT EXISTS users(
        user_id BIGSERIAL PRIMARY KEY,
        username VARCHAR(255) NOT NULL
        );
        """

    INSERT_USER = """
        INSERT INTO users (username, user_id) 
        VALUES ($1, $2) 
        RETURNING user_id;
        """


class CreateDice:
    CREATE_TABLE_DICE = """
        CREATE TABLE IF NOT EXISTS dice(
        user_id BIGINT PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        rolls INTEGER NOT NULL,
        CONSTRAINT fk_user
                   FOREIGN KEY(user_id) 
                   REFERENCES users(user_id)
                   ON DELETE CASCADE
    
        );
        """

    INSERT_DICE = """
        INSERT INTO dice (user_id, username, rolls)
        VALUES ($1, $2, $3)
        ON CONFLICT (user_id) DO NOTHING;
        """


class CreateCharacters:
    CREATE_TABLE_CHARACTERS = """
       CREATE TABLE IF NOT EXISTS characters (
           user_id BIGINT PRIMARY KEY,
           username VARCHAR(255) NOT NULL,
           char_name VARCHAR(255) NOT NULL,
           strength INTEGER NOT NULL,
           dexterity INTEGER NOT NULL,
           constitution INTEGER NOT NULL,
           intelligence INTEGER NOT NULL,
           wisdom INTEGER NOT NULL,
           charisma INTEGER NOT NULL,
           CONSTRAINT fk_user
               FOREIGN KEY(user_id) 
               REFERENCES users(user_id)
               ON DELETE CASCADE
       );
       """

    INSERT_CHARACTER = """
       INSERT INTO characters (user_id, username, char_name, strength, dexterity, constitution, intelligence, wisdom, charisma)
       VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9)
       ON CONFLICT (user_id) DO NOTHING;
       """


class Events:
    CREATE_TABLE_EVENTS = """
        CREATE TABLE IF NOT EXISTS events (
            user_id BIGINT PRIMARY KEY REFERENCES users(user_id) ON DELETE CASCADE,
            username VARCHAR(255) NOT NULL,
            dice INTEGER NOT NULL
            ON CONFLICT (user_id) DO NOTHING;
        
        ); 
    """

    INSERT_EVENT = "INSERT INTO events (user_id, event_name, dice_roll) VALUES ($1, $2, $3) RETURNING id;"


CHECK_USER = "SELECT * FROM users WHERE user_id = $1;"


class WebAppLogin:
    CREATE_TABLE_WEBAPP_LOGINS = """
        CREATE TABLE IF NOT EXISTS webapp_logins (
            user_id BIGINT PRIMARY KEY REFERENCES users(user_id) ON DELETE CASCADE,
            username VARCHAR(255) NOT NULL
        );
        """

    INSERT_USER = """
        INSERT INTO webapp_logins (user_id, username)
        VALUES ($1, $2) 
        RETURNING user_id;
        """

    USER_CHECK = """
        SELECT u.user_id, u.username AS user_username, w.username AS login_username
        FROM users u
        JOIN webapp_logins w ON u.user_id = w.user_id
        WHERE u.user_id = YOUR_USER_ID;
        """


# Example usage for testing connection and table creation
async def initialize_db():
    pool = await create_db_pool()
    async with pool.acquire() as connection:
        await connection.execute(CreateUsers.CREATE_TABLE_USERS)
        await connection.execute(CreateCharacters.CREATE_TABLE_CHARACTERS)
        await connection.execute(CreateDice.CREATE_TABLE_DICE)
        print("Tables created successfully.")
