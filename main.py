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
   
   elif message.content.startswith('$text'):
      await message.channel.send(text)

   elif message.content.startswith('$kurwin'):
      await message.channel.send(kurwin)

   elif message.content.startswith('$dzierg2'):
      await message.channel.send(dzierg2)
   
   elif message.content.startswith('$dzierg'):
      await message.channel.send(dzierg)
   
client.run(token)
