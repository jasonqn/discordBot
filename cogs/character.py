import discord
from discord.ext import commands
from dice import roll_dice, no_double_ones


class RollCharacter(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='random')
    async def character_roll(self, ctx, char_name: str):
        print("character_roll called!")
        try:
            # Roll 4d6 discarding the lowest in each instance
            # Strength roll
            strength = no_double_ones()
            dexterity = no_double_ones()
            constitution = no_double_ones()
            intelligence = no_double_ones()
            wisdom = no_double_ones()
            charisma = no_double_ones()

            # Construct the response
            # response = f"Character Name: {char_name} \n\nStats:\n "
            response = f"Strength: {strength}\n"
            response += f"Dexterity: {dexterity}\n"
            response += f"Constitution: {constitution}\n"
            response += f"Intelligence: {intelligence}\n"
            response += f"Wisdom: {wisdom}\n"
            response += f"Charisma: {charisma}"
            print(response)

            embed_character_creator = discord.Embed(title="Character creator",
                                                    description="Click",
                                                    colour=0xf54900)

            embed_character_creator.add_field(name="Character Name ", value=char_name, inline=False)
            embed_character_creator.add_field(name="Stats Rolled: ", value=response, inline=True)

            await ctx.send(embed=embed_character_creator)
        except Exception as e:
            print(e)


async def setup(bot):
    await bot.add_cog(RollCharacter(bot))
