from discord.ext import commands
from discord.ext.commands import Cog
import config

# import config class for database
clientObj = config.Oauth()
client = clientObj.databaseCONN()
db = client.dnd


class ReactionRoles(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.db = db


    def
