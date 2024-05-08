import config
import discord
from discord.ext import commands
from discord import Message

# import config class for database
# clientObj = config.Oauth()
# client = clientObj.databaseTOKEN()


class PlayerRegistration(commands.cog):

    def __init__(self, bot):
        self.bot = bot
        # self.db = client

    @commands.command(name="register")
    async def register(self, ctx):

        tick = discord.ui.Button(emoji=discord.PartialEmoji.from_str("<:ballot_box_with_check:>"))
        x = discord.ui.Button(emoji=discord.PartialEmoji.from_str("<:regional_indicator_x:>"))
        embed_register = discord.Embed(title="Account Registration",
                                       description=f"Would you like to register an account with DnD Bot? ")
        embed_register.add_field(name="yes", value=tick)
        embed_register.add_field(name="no", value=x)

        try:
            await ctx.send(embed_register)
        except Exception as e:
            print(e)


async def setup(bot):
    await bot.add_cog(PlayerRegistration(bot))
