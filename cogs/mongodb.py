import random
from cogs import config
import pymongo
import string
import discord
from discord.ext import commands
from discord import Message, Emoji, Embed
import datetime

# import config class for database
clientObj = config.Oauth()
client = clientObj.databaseTOKEN()


class PlayerRegistration(commands.cog):

    def __init__(self, bot):
        self.bot = bot
        self.db = client
        self.emoji_tick = discord.utils.get()
        self.user_details = {
            "discord_id": "",
            "user_name": ""
        }

    @commands.command(name="register")
    async def register(self, ctx, message: Message):
        register = ["Register, register"]
        embed_register = discord.Embed(title="Account Registration",
                                       description=f"Would you like to register your account with "
                                                   f"{self.bot.get_emoji()}")
        try:
            if any(word in message for word in register):
                await message.author.send("Would you like to register an account with DnD bot please answer with"
                                          " 'Yes' or 'No'")

        except Exception as e:
            print(e)

    @commands.Cog.listener()
    async def on_message(self, ctx, message: Message):
        if message.author == self.bot:
            return
        register = ["Register, register"]
        msg = message.content.lower()
        if any(word in msg for word in register):
            await message.author.send("Would you like to register an account with DnD bot please answer with"
                                      " 'Yes' or 'No'")


async def setup(bot):
    await bot.add_cog(PlayerRegistration(bot))
