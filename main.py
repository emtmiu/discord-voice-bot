import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)

TOKEN = "YOUR_BOT_TOKEN_HERE"  # Thay bằng token bot Discord của bạn

@bot.event
async def on_ready():
    print(f"{bot.user} đã online!")

@bot.command()
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send("✅ Đã vào kênh thoại!")
    else:
        await ctx.send("❌ Bạn phải vào kênh thoại trước.")

@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("👋 Bot đã rời kênh thoại.")
    else:
        await ctx.send("❌ Bot không ở trong kênh thoại.")

bot.run(TOKEN)
