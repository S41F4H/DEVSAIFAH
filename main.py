import os
import discord
from discord.ext import commands

# ดึง Token จาก Environment Variable
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def test(ctx):
    await ctx.send("บอทพร้อมทำงานแล้ว")

bot.run(TOKEN)
