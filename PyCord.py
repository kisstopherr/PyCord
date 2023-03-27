import discord
from discord.ext import commands
import subprocess

TOKEN = 'MTA4MTk4MjUyOTcwNTM1MzMwNg.G0DVFB.w9AHS5JNEeO_ShF1TdSMGeX58Qr9qny--ePAtg'

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='.', intents=intents)


@client.event
async def on_ready():
    print('bot ready')


@client.command()
async def python(ctx):
    code = ctx.message.content.split('```')[1]
    process = subprocess.Popen(['C:\Program Files\Python310\python.exe', '-c', code], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, errors = process.communicate()
    if output:
        await ctx.send(f"Output:\n```{output.decode('utf-8')}```")
    if errors:
        await ctx.send(f"Errors:\n```{errors.decode('utf-8')}```")



#C:\Program Files\Python310\python.exe
client.run(TOKEN)