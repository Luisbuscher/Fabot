from discord.ext import commands
import discord

class Adm(commands.Cog):
    '''COMANDOS DE ADMINISTRAÇÃO'''
    def __init__(self, bot):
        self.bot = bot

    @commands.command('!delete')
    @commands.has_permissions(manage_messages=True)
    async def delete(self, ctx, qtd=int(0)):
        if qtd == 0:
            await ctx.send('Comando requer argumentos adicionais, entregando a quantidade de mensagem a ser deletada, exemplo: !delete 5')
        elif qtd > 30:
            await ctx.send('Você não pode deletar mais de 30 mensagens por vez, calma o coração!')
        else:
            await ctx.channel.purge(limit=qtd)

    @commands.command('!clear')
    @commands.has_permissions(administrator = True)
    async def clear(self, ctx, qtd=int(100000)):
        await ctx.channel.purge(limit=qtd)

    @commands.command('!kick')
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        if reason == None:
            reason = 'Sem motivo'
        await ctx.guild.kick(member)
        await ctx.send(f'O usuário {member.mention} foi expulso pelo seguinte motivo: {reason}')

    @commands.command('!ban')
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member, *, reason=None):
        if reason == None:
            reason = 'Sem motivo'
        if ctx.author.top_role <= user.top_role:
            await ctx.send('Você não pode banir alguém com cargo maior ou igual ao seu, bobão!')
        if ctx.author.top_role > user.top_role:
            await ctx.guild.ban(user, reason=reason)
            await ctx.send(f'{user} foi banido com sucesso pelo seguinte motivo: {reason}')


def setup(bot):
    bot.add_cog(Adm(bot))