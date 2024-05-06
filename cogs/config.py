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
        self.db_link = "your Mongo database link here"
        self.client = pymongo.MongoClient(self.db_link)

    def discordtoken(self):
        return self.TOKEN, self.OWNER_IDS

    def databasetoken(self):
        return self.client
