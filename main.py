import discord
from discord.ext import commands
import os

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'บอทออนไลน์แล้ว: {bot.user}')

@bot.command()
async def ทดสอบ(ctx):
    await ctx.send("✅ บอทพร้อมใช้งานแล้ว!")

bot.run(TOKEN)