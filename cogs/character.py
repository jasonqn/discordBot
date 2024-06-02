import discord
from discord.ext import commands
from dice import roll_dice, stat_roll_logic


class RollCharacter(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='rollcharacter')
    async def character_roll(self, ctx, char_name: str):
        print("character_roll called!")
        try:
            # Roll 4d6 discarding the lowest in each instance
            # Strength roll
            strength = stat_roll_logic()
            dexterity = stat_roll_logic()
            constitution = stat_roll_logic()
            intelligence = stat_roll_logic()
            wisdom = stat_roll_logic()
            charisma = stat_roll_logic()

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
