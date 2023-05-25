# bot.py
import os
import random
import discord
import functionWeb as fW
import datetime

from discord.ext import commands, tasks
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(intents=intents, command_prefix='!')

@bot.command(name='99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

@bot.command(name='horoscope')
async def horoscope(ctx):

    response = fW.functionGorafi()
    await ctx.send(response)

# creating a loop that runs every day at 3 PM UTC
@tasks.loop(time=datetime.time(hour=12, minute=3))
async def job_loop(channel: discord.TextChannel):
    weekday = datetime.datetime.utcnow().weekday()
    if weekday == 3:    # sunday
        # do your job here
        message = fW.functionGorafi()
        await channel.send(message)

@bot.event
async def on_ready():

    if not job_loop.is_running():
        channel = bot.get_channel(670755529110323222)
        print(f"Got channel : {channel}")
        job_loop.start(channel)

    print('Ready')

bot.run(TOKEN)