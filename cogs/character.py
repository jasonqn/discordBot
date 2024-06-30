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
        # self.roll = no_double_ones()
        self.stat_total = 0
        user_details = {
            "user_id": self.user_id,
            "username": self.username,
            "Character": self.stats
        }

    async def dice_roll_character(self):
        stat = [roll_dice(1, 6) for _ in range(4)]
        stat.sort()
        while stat[0] & stat[1] == 1:
            stat.pop(0)
            new_roll = roll_dice(1, 6)
            stat.insert(0, new_roll)
        lowest_roll = min(stat)
        stat_total = sum(stat) - lowest_roll
        return stat_total

    @commands.command(name='random')
    async def character_roll(self, ctx, char_name: str):
        print("character_roll called!")
        try:
            # Roll 4d6 discarding the lowest in each instance

            strength = await self.dice_roll_character()
            dexterity = await self.dice_roll_character()
            constitution = await self.dice_roll_character()
            intelligence = await self.dice_roll_character()
            wisdom = await self.dice_roll_character()
            charisma = await self.dice_roll_character()
            stats = [strength, dexterity, constitution, intelligence, wisdom, charisma]

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

            view = CharacterButtons(user_id=str(ctx.author.id), username=str(ctx.author), char_name=char_name,
                                    stats=stats)

            await ctx.send(embed=embed_character_creator, view=view)
        except Exception as e:
            print(e)


class CharacterButtons(discord.ui.View):

    def __init__(self, user_id, username, char_name, stats, *, timeout=None):
        super().__init__(timeout=timeout or 180)

        self.collection = collection
        self.registered_users = set()
        self.user_id = str
        self.username = str
        self.character = str
        self.char_name = char_name
        self.stats = stats

    async def button_logic(self, interaction: discord.Interaction):
        print(f"Button clicked by user: {interaction.user.name}")

        # Add the user to the registered users set
        self.registered_users.add(self.user_id)

        # Insert the user details into the database
        user_details = {
            "user_id": interaction.user.id,
            "username": interaction.user.name,
            "char_name": self.char_name,
            "stats": self.stats
        }
        self.collection.insert_one(user_details)
        print("Character created and stored in database:", user_details)

        await interaction.response.send_message(content=f"{interaction.user} character created successfully!", ephemeral=True)

    @discord.ui.button(label="Create Character!", style=discord.ButtonStyle.green)
    async def confirm_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.button_logic(interaction)
        print("button was clicked!")


async def setup(bot):
    await bot.add_cog(RollCharacter(bot))
