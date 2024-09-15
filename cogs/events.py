import discord
import time
from discord.ext import commands

from database.sql_queries import *
from dice import roll_dice
import psycopg


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='events')
    async def roll(self, ctx):
        try:
            user_id = str(ctx.author.id)
            buttons = EventsButtons()
            embed = discord.Embed(title="Downtime events", color=discord.Color.orange())
            embed.add_field(name="Activity", value="Choose your activity by pressing a button below")
            await ctx.send(embed=embed, view=buttons)
        except Exception as e:
            print(e)


class EventsButtons(discord.ui.View):
    def __init__(self, db_connection, *, timeout=None):
        super().__init__(timeout=timeout or 180)
        self.db_connection = db_connection

    async def button_function(self, interaction: discord.Interaction):
        print(f"Button clicked by user: {interaction.user.name}")
        user_id = str(interaction.user.id)
        username = str(interaction.user)
        dice = roll_dice(1, 20)
        user_details = {
            "user_id": user_id,
            "username": username,
            "dice_roll": dice
        }

        try:
            async with self.db_connection.acquire() as connection:
                print(f"Connection made")
                await connection.execute(Events.INSERT_EVENT, *user_details)
            print("Character created and stored in database:", user_details)
            await interaction.response.send_message(content=f"{interaction.user} character created successfully!",
                                                    ephemeral=True)
        except Exception as e:
            print(f"Error inserting character into database: {e}")
            await interaction.response.send_message(content=f"Failed to create character: {e}", ephemeral=True)

        await interaction.response.send_message(f"You rolled a {dice}!", ephemeral=True)

    @discord.ui.button(label="Crafting", style=discord.ButtonStyle.blurple)
    async def crafting_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.button_function(interaction)
        print("Button was clicked!")

    @discord.ui.button(label="Training", style=discord.ButtonStyle.green)
    async def training_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.button_function(interaction)
        print("Button was clicked!")

    @discord.ui.button(label="Carousing", style=discord.ButtonStyle.gray)
    async def carousing_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.button_function(interaction)
        print("Button was clicked!")

    @discord.ui.button(label="Researching", style=discord.ButtonStyle.red)
    async def researching_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.button_function(interaction)
        print("Button was clicked!")

    async def create_crafting_embed(self):
        embed = discord.Embed(title="Crafting Downtime", color=discord.Color.blue())
        embed.add_field(name="Activity", value="Crafting", inline=False)
        embed.add_field(name="Description", value="You spend your downtime crafting a new item or weapon.",
                        inline=False)
        embed.add_field(name="Requirements", value="Proficiency with tools, raw materials", inline=False)
        embed.add_field(name="Time", value="Varies depending on item complexity", inline=False)
        embed.set_footer(text="Happy Crafting!")
        return embed

    def response_crafting_embed(self, username: str):
        dice = roll_dice(1, 20)
        embed = discord.Embed(title="Crafting Downtime", colour=discord.Color.blue())
        embed.add_field(name="Activity", value="Crafting", inline=False)
        embed.add_field(name="Description", value=f"{username} has rolled for crafting! ",
                        inline=False)
        embed.add_field(name="Roll", value="If you accept, please click the roll button below")
        return embed

    def create_training_embed(self):
        embed = discord.Embed(title="Training Downtime", color=discord.Color.green())
        embed.add_field(name="Activity", value="Training", inline=False)
        embed.add_field(name="Description",
                        value="You spend your downtime training to improve your skills or learn new ones.",
                        inline=False)
        embed.add_field(name="Requirements", value="Instructor, training space", inline=False)
        embed.add_field(name="Time", value="At least 10 days", inline=False)
        embed.set_footer(text="Keep Training Hard!")
        return embed

    def create_carousing_embed(self):
        embed = discord.Embed(title="Carousing Downtime", color=discord.Color.red())
        embed.add_field(name="Activity", value="Carousing", inline=False)
        embed.add_field(name="Description", value="You spend your downtime drinking and socializing.", inline=False)
        embed.add_field(name="Requirements", value="Money to spend", inline=False)
        embed.add_field(name="Time", value="1 to 10 days", inline=False)
        embed.set_footer(text="Enjoy the Party!")
        return embed

    def create_research_embed(self):
        embed = discord.Embed(title="Research Downtime", color=discord.Color.purple())
        embed.add_field(name="Activity", value="Research", inline=False)
        embed.add_field(name="Description", value="You spend your downtime researching a specific topic or question.",
                        inline=False)
        embed.add_field(name="Requirements", value="Access to a library or knowledgeable individuals", inline=False)
        embed.add_field(name="Time", value="Varies depending on research complexity", inline=False)
        embed.set_footer(text="Happy Researching!")
        return embed


async def setup(bot):
    await bot.add_cog(Events(bot))
