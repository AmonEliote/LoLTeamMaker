import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

from comandos.c_2v2 import organizar_2v2
from comandos.c_5v5 import organizar_5v5
from comandos.c_comandos import lista_comandos

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!lol ', intents=intents)

# RETORNO DE CONFIRMAÇÃO QUE O BOT FOI INICIALIZADO
@bot.event
async def on_ready():
    print(f'Tropas liberadas!\n{bot.user}')

# FUNÇÃO DE GERAR DUPLAS
@bot.command(name='2v2')
async def organizar_2v2_wrapper(ctx, *args):
    await organizar_2v2(ctx, *args)

# FUNÇÃO DE GERAR TIMES 5V5
@bot.command(name='5v5')
async def organizar_5v5_wrapper(ctx, *args):
    await organizar_5v5(ctx, *args)

# FUNÇÃO PARA LISTAR OS COMANDOS EXISTENTES
@bot.command(name='comandos')
async def lista_comandos_wrapper(ctx):
    await ctx.send(lista_comandos())

bot.run(TOKEN)