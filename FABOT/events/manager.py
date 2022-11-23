from discord.ext import commands


class Manager(commands.Cog):
    '''COMANDOS DE DADOS RPG'''
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if "palavrão" in message.content:
            await message.channel.send(f'Por favor, {message.author}, não fale palavrões!')

            await message.delete()

            await self.bot.process_commands(message)

def setup(bot):
    bot.add_cog(Manager(bot))