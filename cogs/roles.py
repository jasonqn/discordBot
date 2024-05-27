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
            1243485576410300436: [
                (':shield:', 'Paladin'),
                (':crossed_swords:', 'Fighter'),
                (':axe:', 'Barbarian'),
                (':violin:', 'Bard'),
                (':sparkling_heart:', 'Cleric'),
                (':bear:', 'Druid'),
                (':punch:', 'Monk'),
                (':archery:', 'Ranger'),
                (':dagger:', 'Rogue'),
                (':zap:', 'Sorcerer'),
                (':mage:', 'Warlock'),
                (':fire:', 'Wizard')
            ]
        }

    async def on_reaction_add(self, payload: RawReactionActionEvent, r_type=None) -> None:
        if payload.message_id in self.role_emojis.keys():
            for obj in self.role_emojis[payload.message_id]:
                if obj[0] == payload.emoji.name:
                    guild = self.bot.get_guild(payload.guild_id)
                    user = await guild.fetch_member(payload.user_id)
                    role = guild.get_role(obj[1])
                    if role is None:
                        self.bot.ph.warn(f"An invalid role ID ({obj[0]}, {obj[1]}) was provided in `reaction_roles` for"
                                         f" message with ID: {payload.message_id}")
                        self.bot.ph.warn("Not performing any action as result.")
                    elif r_type == "add":
                        await user.add_roles(role)
                    elif r_type == "remove":
                        await user.remove_roles(role)
                    else:
                        self.bot.ph.warn("Invalid reaction type was provided in `process_reaction`.")
                        self.bot.ph.warn("Not performing any action as result.")
                    break

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: RawReactionActionEvent):
        await self.on_reaction_add(payload, "add")

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload: RawReactionActionEvent):
        await self.on_reaction_add(payload, "remove")


async def setup(bot):
    await bot.add_cog(ReactionRoles(bot))
