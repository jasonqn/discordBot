from random import randint
import discord
from discord.ext import commands
from discord.ext.commands import Cog

from database.sql_queries import SQLQueries
from dice import roll_dice

import database_connection


class DiceCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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
            with self.db_connection.cursor() as cursor:
                cursor.execute(SQLQueries.INSERT_EVENT, (roll_entry, "Some Event"))
                self.db_connection.commit()

            await ctx.send(response)
        except Exception as e:
            print(e)


async def setup(bot):
    await bot.add_cog(DiceCog(bot))
