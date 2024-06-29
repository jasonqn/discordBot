import asyncio
import config

import discord
from discord.ext import commands
from discord import client, Intents, Message
from dice import roll_dice, no_double_ones

clientObj = config.Oauth()
client_mongo = clientObj.databaseCONN()
db = client_mongo.dnd
collection = db.character


class RollCharacter(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.collection = collection
        self.user_id = str
        self.username = str
        self.stats = []
        user_details = {
            "user_id": self.user_id,
            "username": self.username,
            "Character": self.stats
        }

    @commands.command(name='random')
    async def character_roll(self, ctx, char_name: str):
        print("character_roll called!")
        try:
            # Roll 4d6 discarding the lowest in each instance

            strength = no_double_ones()
            dexterity = no_double_ones()
            constitution = no_double_ones()
            intelligence = no_double_ones()
            wisdom = no_double_ones()
            charisma = no_double_ones()
            self.stats = [strength, dexterity, constitution, intelligence, wisdom, charisma]

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
                                                    description="Please confirm with (yes/no) if you want to keep this"
                                                                "character.",
                                                    colour=0xf54900)

            embed_character_creator.add_field(name="Character Name ", value=char_name, inline=False)
            embed_character_creator.add_field(name="Stats Rolled: ", value=response, inline=True)

            view = CharacterButtons()

            await ctx.send(embed=embed_character_creator, view=view)
        except Exception as e:
            print(e)


class CharacterButtons(discord.ui.View):

    def __init__(self, *, timeout=None):
        super().__init__(timeout=timeout or 180)

        self.collection = collection
        self.client = client
        self.registered_users = set()
        self.user_id = str
        self.username = str
        self.character = str
        self.stats = []
        self.user_details = {
            "user_id": self.user_id,
            "username": self.username,
            "Character": self.stats
        }

    @discord.ui.button(label="Create Character!", style=discord.ButtonStyle.green)
    async def confirm_button(self, interaction: discord.Interaction, button: discord.ui.Button, strength: str,
                             dexterity: str, constitution: str, intelligence: str, wisdom: str, charisma: str):
        # Check if the user is already registered
        if self.user_id in self.registered_users:
            return await interaction.response.send(content="You have already created a character!", ephemeral=True)

        self.stats = [strength, dexterity, constitution, intelligence, wisdom, charisma]
        # Add the user to the registered users set
        self.registered_users.add(self.user_id)
        self.collection.insert_one(self.user_details)

        await interaction.response.send(content=f"{interaction.user} character created successfully!", ephemeral=True)


async def setup(bot):
    await bot.add_cog(RollCharacter(bot))
