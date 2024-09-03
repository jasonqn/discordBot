from discord.ext import commands

from database.sql_queries import create_db_pool, CreateDice
from dice import roll_dice


class DiceCog(commands.Cog):
    def __init__(self, bot, db_connection):
        self.bot = bot
        self.db_connection = db_connection

    @commands.command(name='roll')
    async def roll(self, ctx, select_dice: int, die_face_selection: int):
        user_id = int(ctx.author.id)
        response = roll_dice(select_dice, die_face_selection)
        roll_entry = {
            "user_id": int(user_id),
            "username": ctx.author.name,
            "rolls": response
        }
        try:
            async with self.db_connection.acquire() as connection:
                print(f"Connection made")
                await connection.execute(CreateDice.INSERT_DICE, roll_entry["user_id"], roll_entry["username"],
                                         roll_entry["rolls"])

            await ctx.send(response)
        except Exception as e:
            print(e)


async def setup(bot):
    db_connection = await create_db_pool()
    await bot.add_cog(DiceCog(bot, db_connection))
