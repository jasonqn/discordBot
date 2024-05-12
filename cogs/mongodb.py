import config
import discord
from discord.ext import commands
from discord import Message


# import config class for database
# clientObj = config.Oauth()
# client = clientObj.databaseTOKEN()


class PlayerRegistration(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        # self.db = client

    @commands.command(name="register")
    async def register(self, ctx):
        try:
            view = Buttons()

            embed_register = discord.Embed(title="Account Registration",
                                           description=f"Would you like to register an account with DnD Bot? ")

            await ctx.send(embed=embed_register, view=view)
        except Exception as e:
            print(e)


class Buttons(discord.ui.View):

    def __init__(self, *, timeout=None):
        super().__init__(timeout=timeout or 180)

        self.registered_users = []

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
