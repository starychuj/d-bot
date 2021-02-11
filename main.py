from modules.database import *
from modules.identity import *
from modules.messages import *
import os
import discord
from discord.ext import commands
webhookName = "icebox246"
bot = commands.Bot(command_prefix='$')
token = os.getenv("DISCORD_TOKEN")
async def sendWebhookMessage(ctx,identity,message):
    if not ctx.author == bot.user:
        allWebhooks = await ctx.channel.webhooks()
        selectedWebhook = None
        for webhook in allWebhooks:
            if webhook.name == webhookName:
                selectedWebhook = webhook
        if selectedWebhook == None:
            selectedWebhook = await ctx.channel.create_webhook(name=webhookName)
        await selectedWebhook.send(message,username=identity["name"],avatar_url=identity["photo_url"])
@bot.command()
async def dzierg(ctx):
    await sendWebhookMessage(ctx,dziergID,dziergText)

@bot.command()
async def dzierg2(ctx):
    await sendWebhookMessage(ctx,dziergID,dziergText2)

@bot.command()
async def text(ctx):
    await sendWebhookMessage(ctx,icebox,filmText)

@bot.command()
async def mouson(ctx):
    await sendWebhookMessage(ctx,mousonID,kurwinText)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Roblox"))
    print("Connected to discord")

@bot.event
async def on_message(ctx):
    if ctx.content.startswith('kamil'):
        await sendWebhookMessage(ctx,spike,getRandomMessage(sMessage,createSession()))
    elif ctx.content.startswith('adam'):
       await sendWebhookMessage(ctx,icebox,getRandomMessage(aMessage,createSession()))
    elif ctx.content.startswith('alek'):
       await sendWebhookMessage(ctx,zawo,alek1)
       await sendWebhookMessage(ctx,zawo,alek2)
    await bot.process_commands(ctx)
bot.run(token)
