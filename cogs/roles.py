import discord
from discord.ext import commands
from discord.components import *
import database_connection


class Roles(commands.Cog):

    def __init__(self, bot):
        super().__init__()
        self.bot = bot
        self.role_names = ["Paladin", "Fighter", "Barbarian",
                           "Bard", "Cleric", "Druid",
                           "Monk", "Ranger", "Rogue",
                           "Sorcerer", "Warlock", "Wizard"]

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


class RoleButtons(discord.ui.View):

    def __init__(self, db_connection, *, timeout=None):
        super().__init__(timeout=timeout or 180)
        self.db_connection = db_connection
        self.permissions = discord.Permissions(send_messages=True,
                                               speak=True,
                                               stream=True,
                                               change_nickname=False,
                                               add_reactions=True
                                               )

    async def assign_role(self, interaction: discord.Interaction, role_name: str):
        role = discord.utils.get(interaction.guild.roles, name=role_name)
        if role is None:
            await interaction.guild.create_role(name=role_name)
            role = discord.utils.get(interaction.guild.roles, name=role_name)

        if role not in interaction.user.roles:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                content=f"Welcome, {interaction.user.mention}, you have chosen {role}!", ephemeral=True)
        else:
            await interaction.response.send_message(
                content=f"You are already an {role}, {interaction.user.mention}!", ephemeral=True)
        await role.edit(reason="Setting role permissions", permissions=self.permissions)

    @discord.ui.button(label="Paladin", style=discord.ButtonStyle.grey, emoji="🛡️")
    async def paladin_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.assign_role(interaction, "Paladin")

    @discord.ui.button(label="Fighter", style=discord.ButtonStyle.grey, emoji="⚔️")
    async def fighter_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.assign_role(interaction, "Fighter")

    @discord.ui.button(label="Barbarian", style=discord.ButtonStyle.grey, emoji="🪓")
    async def Barbarian_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.assign_role(interaction, "Barbarian")

    @discord.ui.button(label="Bard", style=discord.ButtonStyle.grey, emoji="🎻")
    async def Bard_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.assign_role(interaction, "Bard")

    @discord.ui.button(label="Cleric", style=discord.ButtonStyle.grey, emoji="💖")
    async def cleric_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.assign_role(interaction, "Cleric")

    @discord.ui.button(label="Druid", style=discord.ButtonStyle.grey, emoji="🐻")
    async def druid_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.assign_role(interaction, "Druid")

    @discord.ui.button(label="Monk", style=discord.ButtonStyle.grey, emoji="👊")
    async def monk_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.assign_role(interaction, "Monk")

    @discord.ui.button(label="Ranger", style=discord.ButtonStyle.grey, emoji="🏹")
    async def ranger_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.assign_role(interaction, "Ranger")

    @discord.ui.button(label="Rogue", style=discord.ButtonStyle.grey, emoji="🗡️")
    async def rogue_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.assign_role(interaction, "Rogue")

    @discord.ui.button(label="Sorcerer", style=discord.ButtonStyle.grey, emoji="⚡")
    async def sorcerer_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.assign_role(interaction, "Sorcerer")

    @discord.ui.button(label="Warlock", style=discord.ButtonStyle.grey, emoji="🔥")
    async def warlock_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.assign_role(interaction, "Warlock")

    @discord.ui.button(label="Wizard", style=discord.ButtonStyle.grey, emoji="🧙")
    async def wizard_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.assign_role(interaction, "Wizard")


async def setup(bot):
    await bot.add_cog(Roles(bot))
