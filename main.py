import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
discord_token = os.getenv("BOT_TOKEN")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

bot.run(discord_token)