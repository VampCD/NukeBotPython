import discord, os
from discord.ext import commands

# Bot Prefix and such
client = commands.Bot(
  
intents = discord.Intents.all(),

command_prefix = commands.when_mentioned_or('PREFIX'),

case_insensitive=True,

)

# Running the cogs (extensions)
for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')
# Signing in into the bot and running it
client.run('TOKEN')