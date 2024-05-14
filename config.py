import os
from typing import Final
import pymongo
from dotenv import load_dotenv


load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
DB_LINK: Final[str] = os.getenv('MONGO_DB_CONN')


class Oauth:
    def __init__(self):
        load_dotenv()
        self.TOKEN = TOKEN
        self.OWNER_IDS = ['627569347417866271']

        # database token
        self.db_link = DB_LINK
        self.client = pymongo.MongoClient(self.db_link)

    def discordTOKEN(self):
        return self.TOKEN, self.OWNER_IDS

    def databaseCONN(self):
        return self.client

