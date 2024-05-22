from random import randint
import discord
from discord.ext import commands
from discord.ext.commands import Cog

import config

# import config class for database
clientObj = config.Oauth()
client = clientObj.databaseCONN()
db = client.dnd
collection = db.dice_rolls


# dice roll function called into "roll" function below within
# the Dice class
def roll_dice(select_dice: int, die_face_selection: int):
    # how many faces each die will have
    die_face = {
        4: 4,
        6: 6,
        8: 8,
        10: 10,
        12: 12,
        20: 20,
        100: 100
    }

    # amount of dice users can select, max 10
    dice_amount = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    # roll logic
    dice_rolls = [randint(1, die_face[die_face_selection]) for _ in range(select_dice)]

    # total rolls
    total_roll: int = sum(dice_rolls)

    # Format individual rolls
    individual_rolls = ', '.join(str(roll) for roll in dice_rolls)

    # error handling
    if select_dice not in dice_amount:
        return 'You can only roll up to 10 dice, your first input is the number of die you wish to roll'

    if die_face_selection not in die_face:
        return 'Invalid dice selection, only 4, 6, 8, 10, 12, 20, 100 sided die can be selected'

    return total_roll


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
