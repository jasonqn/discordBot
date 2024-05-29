import discord
from discord.ext import commands
from dice import roll_dice

import config

# import config class for database
clientObj = config.Oauth()
client = clientObj.databaseCONN()
db = client.dnd
collection = db.events


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.collection = collection

    @commands.command(name='events')
    async def roll(self, ctx, select_dice: int, die_face_selection: int):
        user_id = str(ctx.author.id)
        user = db.login.find_one({"user_id": user_id})

        if not user:
            await ctx.send("You are not registered. Please register first using the !register command.")
            return

    @commands.command(name='add')
    async def add_event(self, ctx):
        user_id = str(ctx.author.id)
        user = db.login.find_one({"user_id": user_id})
        if not user:
            await ctx.send("You are not registered. Please register first using the !register command.")
            return

    @commands.command(name='delete')
    async def delete_event(self, ctx):
        user_id = str(ctx.author.id)
        user = db.login.find_one({"user_id": user_id})
        if not user:
            await ctx.send("You are not registered. Please register first using the !register command.")
            return
