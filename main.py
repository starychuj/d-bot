from base import *
import os
import random
import discord
client = discord.Client()
token = os.getenv("DISCORD_TOKEN")
@client.event
async def on_ready():
   await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="hentai"))

@client.event
async def on_message(message):
   if message.content.startswith('adam'):
      await message.channel.send(msg[random.randint(0,len(msg)-1)])
client.run(token)