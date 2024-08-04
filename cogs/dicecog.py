from random import randint
import discord
from discord.ext import commands
from discord.ext.commands import Cog

from database.sql_queries import create_db_pool, CreateUsers
from dice import roll_dice

import database_connection


class DiceCog(commands.Cog):
    def __init__(self, bot, db_connection):
        self.bot = bot
        self.db_connection = db_connection

    @commands.command(name='roll')
    async def roll(self, ctx, select_dice: int, die_face_selection: int):
        user_id = str(ctx.author.id)

        try:
            response = roll_dice(select_dice, die_face_selection)
            roll_entry = {
                "user_id": user_id,
                "username": ctx.author.name,
                "rolls": response
            }
            async with self.db_connection.acquire() as connection:
                await connection.execute()

            await ctx.send(response)
        except Exception as e:
            print(e)


async def setup(bot):
    db_connection = await create_db_pool()
    await bot.add_cog(DiceCog(bot, db_connection))
