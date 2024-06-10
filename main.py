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

@bot.event
async def on_ready():
    print(f'Tropas liberadas!\n{bot.user}')
    await bot.tree.sync()

@bot.tree.command(name="2v2", description="Organizar duplas 2v2")
async def organizar_2v2_slash(interaction: discord.Interaction, nomes: str):
    nomes_list = nomes.split()
    await organizar_2v2(interaction, *nomes_list)

@bot.tree.command(name="5v5", description="Organizar times 5v5")
async def organizar_5v5_slash(interaction: discord.Interaction, nomes: str):
    nomes_list = nomes.split()
    await organizar_5v5(interaction, *nomes_list)

@bot.tree.command(name="comandos", description="Lista os comandos existentes")
async def lista_comandos_slash(interaction: discord.Interaction):
    await interaction.response.send_message(lista_comandos())

bot.run(TOKEN)
