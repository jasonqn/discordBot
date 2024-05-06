import random
from cogs import config
import pymongo
import string
import discord
from discord.ext import commands
import datetime

# import config class for database
clientObj = config.Oauth()
client = clientObj.databaseTOKEN()


class PlayerRegistration(commands.cog):

    def __init__(self, bot):
        self.bot = bot
        self.db = client
        self.user_details = {
            "discord_id": "",
            "user_name": ""
        }

    @commands.command(name="register")
    async def register(self, ctx):





