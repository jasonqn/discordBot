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


class Character(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='character_roll')
    async def character_creator(self, ctx, char_name: str):
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
            response = f"Character Name: {char_name} \nStats: "
            response += f"Strength: {strength}\n"
            response += f"Dexterity: {dexterity}\n"
            response += f"Constitution: {constitution}\n"
            response += f"Intelligence: {intelligence}\n"
            response += f"Wisdom: {wisdom}\n"
            response += f"Charisma: {charisma}"
            print(response)
            await ctx.send(response)
        except Exception as e:
            print(e)


async def setup(bot):
    await bot.add_cog(Character(bot))
