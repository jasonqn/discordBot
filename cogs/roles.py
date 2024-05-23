import discord
from discord.ext import commands
from discord import Intents, Message, Reaction, User, Guild, RawReactionActionEvent
from discord.ext.commands import Cog
import config

# import config class for database
clientObj = config.Oauth()
client = clientObj.databaseCONN()
db = client.dnd


class ReactionRoles(Cog):

    def __init__(self, bot):
        super().__init__()
        self.bot = bot
        self.db = db
        self.role_emojis = {
            ':shield:': 'Paladin',
            ':crossed_swords:': 'Fighter',
            ':axe:': 'Barbarian',
            ':violin:': 'Bard',
            ':sparkling_heart:': 'Cleric',
            ':bear:': 'Druid',
            ':punch:': 'Monk',
            ':archery:': 'Ranger',
            ':dagger:': 'Rogue',
            ':zap:': 'Sorcerer',
            ':mage:': 'Warlock',
            ':fire:': 'Wizard'
        }

    async def on_reaction_add(self, payload: RawReactionActionEvent):
        payload.message_id in self.role_emojis.keys()


