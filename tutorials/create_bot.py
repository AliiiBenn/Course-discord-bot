import discord
from discord.ext import commands

import os, dotenv

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

if __name__ == '__main__':
    dotenv.load_dotenv()
    token = os.getenv('token')
    
    if token is None:
        raise ValueError('Token not found')
    
    bot.run(token)