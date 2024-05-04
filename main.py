import asyncio
from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Message
from discord.ext import commands
import sys
from cogs import dicecog

sys.path.insert(0, 'C:/Users/Jason/finance/discordBot/cogs')

# Loads token
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# Bot Setup
intents: Intents = Intents.default()
intents.message_content = True  # NOQA
intents.messages = True  # NOQA

# Bot Command setup
bot = commands.Bot(command_prefix='!', intents=intents)


async def load_extensions():
    for file in os.listdir('cogs'):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                await bot.load_extension(f"cogs.{extension}")
            except Exception as e:
                print(f"Failed to load extension {extension}: {e}")


async def setup_hook() -> None:
    await load_extensions()


@bot.event
async def on_ready() -> None:
    print(f'{bot.user} is now running! :)')
    print(f'{bot.load_extension()} are loaded!')


@bot.event
async def on_message(message: Message) -> None:
    if message.author == bot.user:
        return

    await bot.process_commands(message)

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)
    user_id: str = str(message.id)

    print(f'[{channel}] {user_id} {username}: "{user_message}"')


async def main() -> None:
    await setup_hook()
    await bot.start(TOKEN)


if __name__ == '__main__':
    asyncio.run(main())
