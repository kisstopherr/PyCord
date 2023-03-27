import discord
from discord.ext import commands
import subprocess

TOKEN = 'YOUR TOKEN'

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='.', intents=intents)


@client.event
async def on_ready():
    print('bot ready')


@client.command()
async def python(ctx):
    code = ctx.message.content.split('```')[1]
    process = subprocess.Popen(['PATH/TO/PYTHON.exe', '-c', code], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, errors = process.communicate()
    if output:
        await ctx.send(f"Output:\n```{output.decode('utf-8')}```")
    if errors:
        await ctx.send(f"Errors:\n```{errors.decode('utf-8')}```")


client.run(TOKEN)
