import discord
import time
from discord.ext import commands
from dice import roll_dice

import config

# import config class for database
clientObj = config.Oauth()
client = clientObj.databaseCONN()
db = client.dnd
events_db = db.events
login_db = db.login


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.collection = events_db

    @commands.command(name='events')
    async def roll(self, ctx, select_dice: int, die_face_selection: int):
        user_id = str(ctx.author.id)
        user = db.login.find_one({"user_id": user_id})

        if not user:
            await ctx.send("You are not registered. Please register first using the !register command.")
            return

    # Define embed message templates for D&D downtime events

    def create_crafting_embed(self):
        embed = discord.Embed(title="Crafting Downtime", color=discord.Color.blue())
        embed.add_field(name="Activity", value="Crafting", inline=False)
        embed.add_field(name="Description", value="You spend your downtime crafting a new item or weapon.",
                        inline=False)
        embed.add_field(name="Requirements", value="Proficiency with tools, raw materials", inline=False)
        embed.add_field(name="Time", value="Varies depending on item complexity", inline=False)
        embed.set_footer(text="Happy Crafting!")
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


class EventsButtons(discord.ui.View):

    def __init__(self, *, timeout=None):
        super().__init__(timeout=timeout or 180)
        self.collection = events_db

    @discord.ui.button(label="Roll Dice",style=discord.ButtonStyle.red)
    async def roll_dice_button(self, interaction: discord.Interaction, button: discord.ui.Button):


