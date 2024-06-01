from random import randint
import discord
from discord.ext import commands
from discord.ext.commands import Cog
from dice import roll_dice

import config

# import config class for database
clientObj = config.Oauth()
client = clientObj.databaseCONN()
db = client.dnd
collection = db.dice_rolls


class DiceCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.collection = collection

    @commands.command(name='roll')
    async def roll(self, ctx, select_dice: int, die_face_selection: int):
        user_id = str(ctx.author.id)
        user = db.login.find_one({"user_id": user_id})

        if not user:
            await ctx.send("You are not registered. Please register first using the !register command.")
            return

        try:
            response = roll_dice(select_dice, die_face_selection)
            roll_entry = {
                "user_id": user_id,
                "username": ctx.author.name,
                "rolls": response
            }
            self.collection.insert_one(roll_entry)

            await ctx.send(response)
        except Exception as e:
            print(e)


async def setup(bot):
    await bot.add_cog(DiceCog(bot))
