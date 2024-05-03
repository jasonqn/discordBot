from discord.ext import commands
from dicecog import roll_dice

class Character(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    def get_char_stats(self, strength: int, dexterity: int, constitution: int,
                       intelligence: int, wisdom: int, charisma: int):

        stats_array = {strength, dexterity, constitution, intelligence, wisdom, charisma}

        return stats_array

    def roll_stats(self, select_dice, die_face_selection):
        roll = roll_dice(select_dice, die_face_selection)




    @commands.command(name='character creator')
    async def character_creator(self, ctx, char_name: str):
