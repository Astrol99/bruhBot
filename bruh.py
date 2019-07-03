import discord
from discord.ext import commands
import json

# Extracts token and prefix from resources.json
with open("resources.json") as resources:
    data = json.load(resources)
    TOKEN = data['token']
    PREFIX = data['prefix']