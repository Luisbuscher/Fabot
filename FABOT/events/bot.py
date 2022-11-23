from discord.ext import commands


class Bot(commands.Cog):
    '''COMANDOS DE DADOS RPG'''
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot está online')


def setup(bot):
    bot.add_cog(Bot(bot))