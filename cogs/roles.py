import discord
from discord.ext import commands
from discord import Intents, Message, Reaction, User, Guild, RawReactionActionEvent
from discord.ext.commands import Cog
import config

# import config class for database
clientObj = config.Oauth()
client = clientObj.databaseCONN()
db = client.dnd


class Roles(Cog):

    def __init__(self, bot):
        super().__init__()
        self.bot = bot
        self.db = db

    @commands.command(name="role")
    async def register(self, ctx):
        try:
            # Check if the bot has the necessary permissions
            if not ctx.guild.me.guild_permissions.manage_roles:
                await ctx.send("I don't have the necessary permissions to manage roles.")
                return

            # imports the yes and no buttons below the embed message
            view = RoleButtons()
            embed_register = discord.Embed(title="Role Selection",
                                           description=f"Pick your role ")
            await ctx.send(embed=embed_register, view=view)
        except Exception as e:
            print(e)


class RolePermissions:
    def __init__(self):
        self.permissions = discord.Permissions(send_messages=True,
                                               speak=True,
                                               stream=True,
                                               change_nickname=False,
                                               add_reactions=True
                                               )


class RoleButtons(discord.ui.View):

    def __init__(self, *, timeout=None):
        super().__init__(timeout=timeout or 180)
        self.permissions = RolePermissions().permissions
        self.roles = {'🛡️', 'Paladin',
                      '⚔️', 'Fighter',
                      ':axe:', 'Barbarian',
                      ':violin:', 'Bard',
                      ':sparkling_heart:', 'Cleric',
                      ':bear:', 'Druid',
                      ':punch:', 'Monk',
                      ':archery:', 'Ranger',
                      ':dagger:', 'Rogue',
                      ':zap:', 'Sorcerer',
                      ':mage:', 'Warlock',
                      ':fire:', 'Wizard'
                      }
    """""""""
    @discord.ui.button(style=discord.ButtonStyle.grey, emoji=":shield:")
    async def paladin_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        role = discord.utils.get(interaction.guild.roles, name="Paladin")
        if role is None:
            await interaction.guild.create_role(name="Paladin")
            role = discord.utils.get(interaction.guild.roles, name="Paladin")

        if role not in interaction.user.roles:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                content=f"Welcome, {interaction.user.mention}, you have chosen {role}!", ephemeral=True)
        else:
            await interaction.response.send_message(
                content=f"You are already an {role}, {interaction.user.mention}!", ephemeral=True)
        await role.edit(reason="Setting role permissions", permissions=self.permissions)
        """""""""
    async def on_button_click(self, button, interaction):
        role_name = button.label
        role = discord.utils.get(interaction.guild.roles, name=role_name)
        if role is None:
            await interaction.guild.create_role(name=role_name)
            role = discord.utils.get(interaction.guild.roles, name=role_name)

        if role not in interaction.user.roles:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                content=f"Welcome, {interaction.user.mention}, you have chosen {role}!",
                ephemeral=True
            )
        else:
            await interaction.response.send_message(
                content=f"You are already a {role}, {interaction.user.mention}!",
                ephemeral=True
            )

    async def on_timeout(self):
        self.clear_items()

    def make_buttons(self):
        for role_name, emoji in self.roles.items():
            self.add_item(discord.ui.Button(style=discord.ButtonStyle.grey, label=role_name, emoji=emoji))


async def setup(bot):
    await bot.add_cog(Roles(bot))
