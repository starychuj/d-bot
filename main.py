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
      
   if message.content.startswith('$text'):
      await message.channel.send(text)
   
   if message.content.startswith('$kurwin'):
      await message.channel.send(kurwin)
   
   if message.content.startswith('$dzierg'):
      await message.channel.send(dzierg)
      
   if message.content.startswith('$dzierg2'):
      await message.channel.send(dzierg2)
      
client.run(token)
