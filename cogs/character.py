from discord.ext import commands
from dicecog import roll_dice


def stat_roll_logic(stat):
    stat = [roll_dice(1, 6) for _ in range(4)]
    stat.sort()
    while stat[0] & stat[1] == 1:
        stat.pop(0)
        new_roll = roll_dice(1, 6)
        stat.insert(0, new_roll)
    lowest_roll = min(stat)
    stat_total = sum(stat) - lowest_roll
    return stat_total


class Character(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='character_roll')
    async def character_creator(self, ctx, char_name: str):
        print("character_roll called!")
        try:
            # Roll 4d6 discarding the lowest in each instance
            # Strength roll
            stat_roll_logic()

            # Dexterity roll
            dexterity = [roll_dice(1, 6) for _ in range(4)]
            dexterity.sort()
            while dexterity[0] & dexterity[1] == 1:
                if dexterity[0] & dexterity[1] == 1:
                    dexterity.pop(0)
                    new_roll = roll_dice(1, 6)
                    dexterity.insert(0, new_roll)
            lowest_die_dexterity = min(dexterity)
            dexterity_total = sum(dexterity) - lowest_die_dexterity

            # Constitution roll
            constitution = [roll_dice(1, 6) for _ in range(4)]
            constitution.sort()
            while constitution[0] & constitution[1] == 1:
                if constitution[0] & constitution[1] == 1:
                    constitution.pop(0)
                    new_roll = roll_dice(1, 6)
                    constitution.insert(0, new_roll)
            lowest_die_constitution = min(constitution)
            constitution_total = sum(constitution) - lowest_die_constitution

            # Intelligence roll
            intelligence = [roll_dice(1, 6) for _ in range(4)]
            intelligence.sort()
            while intelligence[0] & intelligence[1] == 1:
                if intelligence[0] & intelligence[1] == 1:
                    intelligence.pop(0)
                    new_roll = roll_dice(1, 6)
                    intelligence.insert(0, new_roll)
            lowest_die_intelligence = min(intelligence)
            intelligence_total = sum(intelligence) - lowest_die_intelligence

            # Wisdom roll
            wisdom = [roll_dice(1, 6) for _ in range(4)]
            wisdom.sort()
            while wisdom[0] & wisdom[1] == 1:
                if wisdom[0] & wisdom[1] == 1:
                    wisdom.pop(0)
                    new_roll = roll_dice(1, 6)
                    wisdom.insert(0, new_roll)
            lowest_die_wisdom = min(wisdom)
            wisdom_total = sum(wisdom) - lowest_die_wisdom

            # Charisma roll
            charisma = [roll_dice(1, 6) for _ in range(4)]
            charisma.sort()
            while charisma[0] & charisma[1] == 1:
                if charisma[0] & charisma[1] == 1:
                    charisma.pop(0)
                    new_roll = roll_dice(1, 6)
                    charisma.insert(0, new_roll)
            lowest_die_charisma = min(charisma)
            charisma_total = sum(charisma) - lowest_die_charisma

            # Construct the response
            response = f"Character Name: {char_name} \nStats: "
            response += (f"Strength: {strength_total}, you rolled {strength} taking the lowest roll away "
                         f"of : {lowest_die_strength}\n ")

            response += (f"Dexterity: {dexterity_total}, you rolled {dexterity} taking the lowest roll away "
                         f"of : {lowest_die_dexterity}\n ")

            response += (f"Constitution: {constitution_total}, you rolled {constitution} taking the lowest roll away "
                         f"of : {lowest_die_constitution}\n")

            response += (f"Intelligence: {intelligence_total}, you rolled {intelligence} taking the lowest roll away "
                         f"of : {lowest_die_intelligence}\n")

            response += (f"Wisdom: {wisdom_total}, you rolled {wisdom} taking the lowest roll away "
                         f"of : {lowest_die_wisdom}\n")

            response += (f"Charisma: {charisma_total}, you rolled {charisma} taking the lowest roll away"
                         f" of : {lowest_die_charisma}")
            print(response)
            await ctx.send(response)
        except Exception as e:
            print(e)


async def setup(bot):
    await bot.add_cog(Character(bot))
