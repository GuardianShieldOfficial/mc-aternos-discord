import discord
from discord.ext import commands
from python_aternos import Client
import asyncio
import os

# --- Configuration ---
DISCORD_TOKEN = 'paste-your-token-here'
ATERNOS_USERNAME = 'your-aternos-username'
ATERNOS_PASSWORD = 'your-aternos-password'
SERVER_DOMAIN = 'yourservername.aternos.me'
COMMAND_CHANNEL = 'bot-cmnds'

# --- Discord Setup ---
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', intents=intents)

# --- Aternos Setup ---
aternos = Client(ATERNOS_USERNAME, password=ATERNOS_PASSWORD)
my_server = aternos.servers[0]  # Use the first server


@bot.event
async def on_ready():
    print(f'✅ Logged in as {bot.user}')


# --- Commands ---
@bot.command(name='server_start')
async def server_start(ctx):
    if ctx.channel.name != COMMAND_CHANNEL:
        return

    embed = discord.Embed(
        title="🟡 Starting Server...",
        description="Please wait while the Aternos server is starting...",
        color=discord.Color.gold()
    )
    await ctx.send(embed=embed)

    my_server.start()

    for _ in range(120):  # check every 5s, up to 2 mins
        await asyncio.sleep(5)
        status = os.popen(f'mcstatus {SERVER_DOMAIN} status').read()
        if 'online' in status.lower():
            embed = discord.Embed(
                title="✅ Server Online!",
                description=f"The server is now online.\nJoin using:\n`{SERVER_DOMAIN}`\n\n*It may take a couple minutes to fully load.*",
                color=discord.Color.green()
            )
            await ctx.send(embed=embed)
            return

    embed = discord.Embed(
        title="❌ Server Startup Timeout",
        description="The server did not start in time. Please try again later.",
        color=discord.Color.red()
    )
    await ctx.send(embed=embed)


@bot.command(name='server_stop')
async def server_stop(ctx):
    if ctx.channel.name != COMMAND_CHANNEL:
        return

    my_server.stop()
    embed = discord.Embed(
        title="🛑 Server Stopped",
        description="The server has been shut down.",
        color=discord.Color.red()
    )
    await ctx.send(embed=embed)


# --- Run the Bot ---
bot.run(DISCORD_TOKEN)
