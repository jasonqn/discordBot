import asyncio
import config

import discord
from discord.ext import commands
from discord import client
from dice import roll_dice, no_double_ones

clientObj = config.Oauth()
client_mongo = clientObj.databaseCONN()
db = client_mongo.dnd
collection = db.character


class RollCharacter(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.collection = collection

    @commands.command(name='random')
    async def character_roll(self, ctx, char_name: str, message: discord.Message):
        print("character_roll called!")
        user_id = str(message.author.id)
        username = str(message.author.name)
        character = str
        user_details = {
            "user_id": user_id,
            "username": username,
            "Character": character
        }
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

            character = response

            embed_character_creator = discord.Embed(title="Character creator",
                                                    description="Please confirm with (yes/no) if you want to keep this"
                                                                "character.",
                                                    colour=0xf54900)

            embed_character_creator.add_field(name="Character Name ", value=char_name, inline=False)
            embed_character_creator.add_field(name="Stats Rolled: ", value=response, inline=True)

            await ctx.send(embed=embed_character_creator)

            try:
                confirmation = await client.wait_for('message', timeout=30.0)
            except asyncio.TimeoutError:  # returning after timeout
                return

            if confirmation.content.lower() not in ("yes", "y"):
                return ctx.send(content="Character not created")
            else:
                self.collection.insert_one(user_details)
                return ctx.send(content="Character created!")

        except Exception as e:
            print(e)


async def setup(bot):
    await bot.add_cog(RollCharacter(bot))
