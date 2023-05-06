import os
import discord
from discord_slash import SlashCommand, SlashContext

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)
slash = SlashCommand(client, sync_commands=True)

@slash.slash(name="hello", description="Says hello")
async def hello(ctx: SlashContext):
    await ctx.send("Hello, world!")

token = os.getenv('TOKEN') or 'your_bot_token_here'
client.run(token)
