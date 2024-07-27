import asyncio

from dotenv import load_dotenv
from psycopg.rows import dict_row

import database_connection
import os
import discord
from discord.ext import commands
from discord import client, Intents, Message
from dice import *
from database.sql_queries import create_db_pool, CreateCharacters
import psycopg


class RollCharacter(commands.Cog):

    def __init__(self, bot, db_connection):
        self.bot = bot
        self.stats = []
        self.stat_total = 0
        self.db_connection = db_connection

    @commands.command(name='random')
    async def character_roll(self, ctx, char_name: str):
        print("character_roll called!")

        try:
            # Roll 4d6 discarding the lowest in each instance

            strength = await dice_roll_character()
            dexterity = await dice_roll_character()
            constitution = await dice_roll_character()
            intelligence = await dice_roll_character()
            wisdom = await dice_roll_character()
            charisma = await dice_roll_character()
            stats = {"Strength": strength,
                     "Dexterity": dexterity,
                     "Constitution": constitution,
                     "Intelligence": intelligence,
                     "Wisdom": wisdom,
                     "Charisma": charisma}

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
                                                    description="Please confirm with (yes/no) if you want to keep "
                                                                "this"
                                                                "character.",
                                                    colour=0xf54900)

            embed_character_creator.add_field(name="Character Name ", value=char_name, inline=False)
            embed_character_creator.add_field(name="Stats Rolled: ", value=response, inline=True)

            view = CharacterButtons(user_id=str(ctx.author.id), username=str(ctx.author), char_name=char_name,
                                    stats=stats, connection=self.db_connection)

            await ctx.send(embed=embed_character_creator, view=view)
        except Exception as e:
            print(e)


class CharacterButtons(discord.ui.View):

    def __init__(self, user_id, username, char_name, stats, connection, *, timeout=None):
        super().__init__(timeout=timeout or 180)
        self.db_connection = connection
        self.user_id = user_id
        self.username = username
        self.char_name = char_name
        self.stats = stats

    async def button_logic(self, interaction: discord.Interaction):
        print(f"Button clicked by user: {interaction.user.name}")

        # Insert the user details into the database
        user_details = {
            "user_id": interaction.user.id,
            "username": interaction.user.name,
            "char_name": self.char_name,
            "stats": self.stats
        }

        async with self.db_connection.acquire() as connection:
            await connection.execute(CreateCharacters.INSERT_CHARACTER, *user_details.values())
        print("Character created and stored in database:", user_details)
        await interaction.response.send_message(content=f"{interaction.user} character created successfully!",
                                                ephemeral=True)

    @discord.ui.button(label="Create Character!", style=discord.ButtonStyle.green)
    async def confirm_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.button_logic(interaction)
        print("button was clicked!")


# Initialize bot and add cogs
async def setup(bot):
    db_pool = await create_db_pool()
    await bot.add_cog(RollCharacter(bot, db_pool))
