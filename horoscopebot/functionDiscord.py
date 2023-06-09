# bot.py
import os
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

@bot.command(name='horoscope')
async def horoscope(ctx):

    response = fW.functionGorafi()
    await ctx.send(response)

# creating a loop that runs every day at 3 PM UTC
@tasks.loop(time=datetime.time(hour=9, minute=3))
async def job_loop(channel: discord.TextChannel):
    weekday = datetime.datetime.utcnow().weekday()
    if weekday == 3:    # sunday
        # do your job here
        message = fW.functionGorafi()
        await channel.send(message)

@bot.event
async def on_ready():

    if not job_loop.is_running():
        channel = bot.get_channel(433156823189684224)
        print(f"Got channel : {channel}")
        job_loop.start(channel)

    print('Ready to bot')

bot.run(TOKEN)