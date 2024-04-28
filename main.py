from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Message
from discord.ext import commands
from responses import *

# Loads token
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# Bot Setup
intents: Intents = Intents.default()
intents.message_content = True  # NOQA
intents.messages = True  # NOQA

bot = commands.Bot(command_prefix='!', intents=intents)
print(bot.command_prefix)


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    print("Add command called")  # Debugging statement
    try:
        result = left + right
        await ctx.send(f"The sum of {left} and {right} is: {result}")
    except Exception as e:
        print(e)


async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print("(Message was empty due to intents not being enabled)")
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


@bot.command()
async def roll(ctx, select_dice: int, die_face_selection: int):
    print("Roll command call")
    try:
        response = roll_dice(select_dice, die_face_selection)
        if response:  # Check if response is not empty
            await ctx.send(response)
        else:
            await ctx.send("Invalid input for dice roll.")  # Send error message
    except Exception as e:
        print(e)


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
