import config
import discord
from discord.ext import commands
from discord import Message
import pymongo


# import config class for database
clientObj = config.Oauth()
client = clientObj.databaseCONN()
db = client.dnd
collection = db.login


class PlayerRegistration(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.collection = collection

    @commands.command(name="register")
    async def register(self, ctx):
        try:
            # imports the yes and no buttons below the embed message
            view = Buttons()
            embed_register = discord.Embed(title="Account Registration",
                                           description=f"Would you like to register an account with DnD Bot? ")
            await ctx.send(embed=embed_register, view=view)
        except Exception as e:
            print(e)


# creates buttons
class Buttons(discord.ui.View):

    def __init__(self, *, timeout=None):
        super().__init__(timeout=timeout or 180)

        self.client = client
        self.collection = collection
        self.post = {}

    def insert_data(self, message: Message):
        user_id: str = str(message.id)
        username: str = str(message.author)
        self.post = {
            "user_id": user_id,
            "username": username
        }
        register_user = self.post

    @discord.ui.button(label="Yes", style=discord.ButtonStyle.green)
    async def yes_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        # checks if the user has already registered
        if interaction.user in self.registered_users:
            return await (interaction.response.send_message
                          (content="User already registered!", ephemeral=True))

        self.registered_users.append(interaction.user)  # add the user to register list

    @discord.ui.button(label="No", style=discord.ButtonStyle.red)
    async def no_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user in self.registered_users:
            return await interaction.response.send_message(content="User already registered!", ephemeral=True)
        return




async def setup(bot):
    await bot.add_cog(PlayerRegistration(bot))
