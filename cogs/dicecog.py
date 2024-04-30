
from discord.ext import commands

from discord.ext.commands import Cog
from responses import *


# dice roll function called into "roll" function below within
# the Dice class
def roll_dice(select_dice: int, die_face_selection: int):
    # how many faces each die will have
    die_face = [4, 6, 8, 10, 12, 20, 100]
    # amount of dice users can select, max 10
    dice_amount = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    # roll logic
    dice_roll = select_dice * (randint(1, die_face_selection))

    # error handling
    if select_dice not in dice_amount:
        return 'You can only roll up to 10 dice, your first input is the number of die you wish to roll'

    if die_face_selection not in die_face:
        return 'Invalid dice selection, only 4, 6, 8, 10, 12, 20, 100 sided die can be selected'

    # successful output
    return f'You chose {select_dice}  dice with {die_face_selection} faces giving you {dice_roll}'


class DiceCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='roll')
    async def roll(self, ctx, select_dice: int, die_face_selection: int):
        print("Roll command call")
        try:
            response = roll_dice(select_dice, die_face_selection)
            await ctx.send(response)
        except Exception as e:
            print(e)


def setup(bot):
    bot.add_cog(DiceCog(bot))
