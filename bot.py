import discord
from discord.ext import commands
from db import get_user, add_user
from riot_api import get_match_data
from scheduler import schedule_weekly_summary

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is online as {bot.user}')
    schedule_weekly_summary(bot)

@bot.command()
async def register(ctx):
    # In echtem Bot: Redirect zu OAuth Flow
    await ctx.send("Please authenticate via Riot here: https://riotgames.com/oauth")

@bot.command()
async def notify(ctx, mode: str):
    if mode not in ["every_match", "weekly"]:
        await ctx.send("Usage: !notify [every_match|weekly]")
        return
    add_user(ctx.author.id, mode)
    await ctx.send(f"Notification mode set to: {mode}")

@bot.command()
async def stats(ctx):
    user = get_user(ctx.author.id)
    if not user:
        await ctx.send("You are not registered. Use !register first.")
        return
    data = get_match_data(user["puuid"])
    await ctx.send(f"Last match: Map: {data['map']}, K/D: {data['kdr']}")

bot.run("YOUR_DISCORD_BOT_TOKEN")