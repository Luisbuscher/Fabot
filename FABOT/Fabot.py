import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='', intents=discord.Intents.all())

bot.load_extension("commands.adm")
bot.load_extension("commands.rpg")
bot.load_extension("commands.geral")
bot.load_extension("events.bot")
bot.load_extension("events.manager")

bot.run('MTAxMTExMjYwNjQ5MDE4NTg5OA.GmKSfR.pUl7yC6TkpNYPSN4-zGjNEQ4KGiAUOJBe8uYCQ')
