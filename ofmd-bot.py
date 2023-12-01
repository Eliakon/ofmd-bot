# coding:utf8

import os, asyncio
import discord
from discord.ext import commands, tasks
from datetime import datetime, timedelta
from dotenv import load_dotenv
import moment

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
TUESDAY_IMG_URL = "https://i.ibb.co/Z2zjY10/tuesday.png"

intents = discord.Intents.default()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    send_tuesday_img.start()

def get_next_scheduled_time():
    target_time = moment.utcnow().zero.add(day=1).replace(hours=5)
    while target_time.weekday != 2:
        target_time.add(day=1)
    return target_time

@tasks.loop(seconds=1)
async def send_tuesday_img():
    next_scheduled_time = get_next_scheduled_time()
    diff = (next_scheduled_time - moment.utcnow()).total_seconds() 
    await asyncio.sleep(diff)
    
    channel = [channel for guild in client.guilds for channel in guild.text_channels][0]
    embed = discord.Embed()
    embed.set_image(url=TUESDAY_IMG_URL)
    await channel.send(embed=embed)

client.run(TOKEN)