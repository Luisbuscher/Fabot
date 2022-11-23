from discord.ext import commands
from random import randint

curiosidade = []

curiosidade.append("GATOS:Para não pisarem em algo perigoso. Os gatos pisam com as patas da frente, as patas de trás pisam no mesmo lugar, pois lá já foi testado.")
curiosidade.append("DINOSSAURO: Dino vem de deinos que significa terrível em grego e sauros é lagarto.")
curiosidade.append("DES: DES em latim significa negativo, por isso na maioria das coisas como DESligar DESfazer e como se DES fosse uma negação.")
curiosidade.append("RAIO VIOLETA: Transmite um raio na terra ruim para os humanos so q ele n consegue transmitir tudo por conta de uma camada protetora na terra e o sol tbm, porém, ainda assim transmite metade e algumas pessoas podem acabar contendo câncer ou casos piores por conta disso.")
curiosidade.append("DIA: O dia tem aproximadamente 23 horas e 56 minutos, não 24 horas. Por isso, a cada quatro anos, adicionamos um dia ao mês de fevereiro. Esses anos são chamados de bissextos.")
curiosidade.append("ARANHAS: As aranhas não possuem ossos, Elas se movimentam a partir de suas patas com o sangue que corre nelas, ou seja, quando você mata uma aranha e muito normal que as patas delas encolham, já que o sangue no qual elas usavam para se movimentar não funciona mais.")
curiosidade.append("CURIOSIDADE: A palavra curiosidade vem do latim (curiositas) que significa desejo por conhecimento.")
curiosidade.append("TELE: A palavra tele vem do grego que significa longe utilizado com 1 nome e juntado com um verbo. Ex: TELEfone, TELEvisao, TELEtransporte, etc...")
curiosidade.append("BICHOS PREGUIÇAS: Elas são tão preguiçosas que ao invés de tentar achar novos parceiros, elas apenas gritam para que eles venham até ela")
curiosidade.append('CÓCEGAS /RISADAS:As cócegas antigamente eram consideradas como método de tortura, principalmente por ser um método prático. Tanto q sorrir antes era um ato de bruxaria. Depois de alguns tempos o sorriso e risada foi tomando forma e sendo considerado "mais normal". Porém, ainda assim as pessoas nunca sorriam nas fotos ou então faziam um sorriso de canto sem mostrar os dentes')

class Geral(commands.Cog):
    '''COMANDOS GERAIS DO BOT'''
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='!ping')
    async def ping(self, ctx):
        await ctx.reply('Pong')

    @commands.command(name='!oi')
    async def mandar_oi(self, ctx):
        name = ctx.author.name
        resposta = 'Olá, '+name

        await ctx.send(resposta)

    @commands.command(name='!curiosidades')
    async def curious(self, ctx):
        sortear = randint(0,9)
        await ctx.reply(f'CURIOSIDADE DA VEZ É:\n\n{curiosidade[sortear]}')

            
def setup(bot):
    bot.add_cog(Geral(bot))