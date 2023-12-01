# coding:utf8

import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
TUESDAY_IMG_URL = "https://i.ibb.co/Z2zjY10/tuesday.png"

intents = discord.Intents.default()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    await send_tuesday_img()

async def send_tuesday_img():
    channel = [channel for guild in client.guilds for channel in guild.text_channels][0]
    print(channel)
    embed = discord.Embed()
    embed.set_image(url=TUESDAY_IMG_URL)
    await channel.send(embed=embed)

client.run(TOKEN)# coding:utf8
