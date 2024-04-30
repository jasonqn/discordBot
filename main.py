from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Message
from discord.ext import commands


# Loads token
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# Bot Setup
intents: Intents = Intents.default()
intents.message_content = True  # NOQA
intents.messages = True  # NOQA

# Bot Command setup
bot = commands.Bot(command_prefix='!', intents=intents)

bot.load_extension('cogs.dicecog')


@bot.event
async def on_ready() -> None:
    print(f'{bot.user} is now running! :)')


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


def main() -> None:
    bot.run(token=TOKEN)


if __name__ == '__main__':
    main()

