import random
import asyncio
import discord
from discord.ext import commands
from basicCommands import HelpCog
from discordToken import *

description = """
A lil Discord bot (under construction)
"""

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"), description=description, intents=intents, help_command=None)
bot.add_cog(HelpCog(bot))

@bot.event
#when u launch the bot, it will print out to the console
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")

@bot.command()
async def add(ctx: commands.Context, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(str(left + right)) #gets the context and send the message into the right channel.
    #await -> waits for the threading to send the message
#ctx = context, what ppl describe the channel ure tryna send the message in

bot.run(TOKEN)