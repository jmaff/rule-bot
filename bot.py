import discord
import config
import rules as r

from discord.ext import commands
import random

description = '''Random bot i made just now'''
bot = commands.Bot(command_prefix='/', description=description)



@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')





@bot.command()
async def (*, rule : str):
    await bot.say(r.rules[rule])  







bot.run(config.token)
