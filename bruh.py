import discord
from discord.ext import commands
import time
import json
import os

# Extracts token and prefix from resources.json
with open("resources.json") as resources:
    data = json.load(resources)
    TOKEN = data['token']
    PREFIX = data['prefix']

# Function to clear console
def clearConsole():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# Add slow printing animation
def aniPrint(message):
    time.sleep(0.5)
    print(message)

# Create bot object
bot = commands.Bot(command_prefix=PREFIX)

@bot.event # Runs this function when bot is started
async def on_ready():
    # Info from bot
    print("[*] Initalizing...")
    time.sleep(3)
    clearConsole()
    bruh = """
    ____             __       ____        __ 
   / __ )_______  __/ /_     / __ )____  / /_
  / __  / ___/ / / / __ \   / __  / __ \/ __/
 / /_/ / /  / /_/ / / / /  / /_/ / /_/ / /_  
/_____/_/   \__,_/_/ /_/  /_____/\____/\__/
                Version 1.0
              Made By: David
"""
    print(bruh)
    time.sleep(2)
    aniPrint("INFO__________________________________")
    aniPrint(f"Prefix: '{PREFIX}'")
    aniPrint(f"discord.py: v{discord.__version__}")
    aniPrint(f"Latency: {round(bot.latency*100)} ms")
    aniPrint(f"Logged in as: {bot.user}")
    aniPrint(f"Bot ID: {bot.user.id}")
    aniPrint(f"Servers connected: {len(bot.guilds)}")

bot.run(TOKEN)