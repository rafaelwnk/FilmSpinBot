import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from cogs.film_cog import FilmCog
from services.film_service import FilmService

load_dotenv()
discord_token = os.getenv("BOT_TOKEN")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)
service = FilmService()
cog = FilmCog(service)

@bot.event
async def on_ready():
    await bot.add_cog(cog)
    await bot.tree.sync()
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="!h"))

bot.run(discord_token)