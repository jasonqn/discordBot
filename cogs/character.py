import discord
from discord.ext import commands
from dicecog import roll_dice


def stat_roll_logic():
    stat = [roll_dice(1, 6) for _ in range(4)]
    stat.sort()
    while stat[0] & stat[1] == 1:
        stat.pop(0)
        new_roll = roll_dice(1, 6)
        stat.insert(0, new_roll)
    lowest_roll = min(stat)
    stat_total = sum(stat) - lowest_roll
    return (f"{stat_total}, you rolled {stat} taking the lowest roll away "
            f"of : {lowest_roll}\n ")


class RollCharacter(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='character_roll')
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
                                                    description="View of rolled stats for created character",
                                                    colour=0xf54900)

            embed_character_creator.add_field(name="Character Name ", value=char_name, inline=False)
            embed_character_creator.add_field(name="Stats Rolled: ", value=response, inline=True)

            await ctx.send(embed=embed_character_creator)
        except Exception as e:
            print(e)


class MakeCharacter(discord.ui.Modal, title="Character Creator"):
    first_name = discord.ui.TextInput(
        label="First Name",
        placeholder="First name here..."
    )

    last_name = discord.ui.TextInput(
        label="Last Name",
        placeholder="Last name here..."
    )


async def setup(bot):
    await bot.add_cog(RollCharacter(bot))
