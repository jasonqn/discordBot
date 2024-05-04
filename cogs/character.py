from discord.ext import commands
from dicecog import roll_dice


class Character(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='character_roll')
    async def character_creator(self, ctx, char_name: str):
        print("character_roll called!")
        try:
            # Roll 4d6 discarding the lowest in each instance
            # Strength roll
            strength: list[int] = [roll_dice(1, 6) for _ in range(4)]
            print(type(strength))
            lowest_die_strength: int = int(min(strength))
            print(type(lowest_die_strength))
            strength_total = sum(strength) - lowest_die_strength
            print(type(strength_total))

            # Dexterity roll
            dexterity = [roll_dice(1, 6) for _ in range(4)]
            lowest_die_dexterity = min(dexterity)
            dexterity_total = sum(dexterity) - lowest_die_dexterity

            # Constitution roll
            constitution = [roll_dice(1, 6) for _ in range(4)]
            lowest_die_constitution = min(constitution)
            constitution_total = sum(constitution) - lowest_die_constitution

            # Intelligence roll
            intelligence = [roll_dice(1, 6) for _ in range(4)]
            lowest_die_intelligence = min(intelligence)
            intelligence_total = sum(intelligence) - lowest_die_intelligence

            # Wisdom roll
            wisdom = [roll_dice(1, 6) for _ in range(4)]
            lowest_die_wisdom = min(wisdom)
            wisdom_total = sum(wisdom) - lowest_die_wisdom

            # Charisma roll
            charisma = [roll_dice(1, 6) for _ in range(4)]
            lowest_die_charisma = min(charisma)
            charisma_total = sum(charisma) - lowest_die_charisma

            # Construct the response
            response = f"Character Name: {char_name} \nStats: "
            response += f"Strength: {strength_total} taking the lowest roll away of :{lowest_die_strength}\n "
            response += f"Dexterity: {dexterity_total} taking the lowest roll away of :{lowest_die_dexterity}\n "
            response += f"Constitution: {constitution_total} taking the lowest roll away of :{lowest_die_constitution}\n "
            response += f"Intelligence: {intelligence_total} taking the lowest roll away of :{lowest_die_intelligence}\n "
            response += f"Wisdom: {wisdom_total} taking the lowest roll away of :{lowest_die_wisdom}\n "
            response += f"Charisma: {charisma_total} taking the lowest roll away of :{lowest_die_charisma}"
            print(response)
            await ctx.send(response)
        except Exception as e:
            print(e)


async def setup(bot):
    await bot.add_cog(Character(bot))
