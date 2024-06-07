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
            # Check if the bot has the necessary permissions
            if not ctx.guild.me.guild_permissions.manage_roles:
                await ctx.send("I don't have the necessary permissions to manage roles.")
                return

            # imports the yes and no buttons below the embed message
            view = RegisterButtons()
            embed_register = discord.Embed(title="Account Registration",
                                           description=f"Would you like to register an account with DnD Bot? ")
            await ctx.send(embed=embed_register, view=view)
        except Exception as e:
            print(e)



    @commands.Cog.listener()
    async def on_member_join(self,ctx):



# creates buttons
class RegisterButtons(discord.ui.View):

    def __init__(self, *, timeout=None):
        super().__init__(timeout=timeout or 180)

        self.collection = collection
        self.client = client
        self.registered_users = set()

    @discord.ui.button(label="Yes", style=discord.ButtonStyle.green)
    async def yes_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        user_id = str(interaction.user.id)
        username = str(interaction.user)
        user_details = {
            "user_id": user_id,
            "username": username
        }

        # Check if the user is already registered
        if user_id in self.registered_users:
            return await interaction.response.send_message(content="User already registered!", ephemeral=True)

        # Add the user to the registered users set
        self.registered_users.add(user_id)

        self.collection.insert_one(user_details)

        await interaction.response.send_message(content=f"{interaction.user} registered successfully!", ephemeral=True)

    @discord.ui.button(label="No", style=discord.ButtonStyle.red)
    async def no_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user:
            return interaction.response(content="User not registered!", ephemeral=True)



async def setup(bot):
    await bot.add_cog(PlayerRegistration(bot))
