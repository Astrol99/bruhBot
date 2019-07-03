import discord
from discord.ext import commands
import json

# Extracts token and prefix from resources.json
with open("resources.json") as resources:
    data = json.load(resources)
    TOKEN = data['token']
    PREFIX = data['prefix']

# Create bot object
bot = commands.Bot(command_prefix=PREFIX)

@bot.event # Runs this function when bot is started
async def on_ready():
    # Info from bot
    print("Bot online!")
    print(f"\nTOKEN: {TOKEN}")
    print(f"PREFIX: {PREFIX}")

bot.run(TOKEN)