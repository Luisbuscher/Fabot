from discord.ext import commands
from random import randint
import mysql.connector

#Id estão errados:
rafa = 5922230102986
filipe = 856658555136
gere = 375483024
malcolm = 8523445906974
dudu = 441627381642

desc = ['Nome do Player:', 'Nome da Personagem:', 'Classe:', 'Raça:', 'Armadura:', 'Euroloso:', 'Vida atual:', 'Vida total:']

con = mysql.connector.connect(host='localhost', database='fabotsql', user='root', password='Universo05@')

if con.is_connected():
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print (f'Conectado ao banco de dados {linha} em RPG')



class Rpg(commands.Cog):
    '''COMANDOS RPG DO BOT'''
    def __init__(self, bot):
        self.bot = bot

    #COMANDO DOS PLAYERS PARA VER A FICHA DE FABULANDIA:

    @commands.command('!ficha')
    async def banco(self, ctx):
        if ctx.author.id == rafa:
            cont = 0
            cursor.execute("select * from players where nome_player='Rafa'")
            linha = cursor.fetchone()
            resposta = ''
            for i in linha:
                print(f'{desc[cont]} {i}')
                resposta += f'{desc[cont]} {i}\n'
                cont += 1
            await ctx.send(resposta)

        if ctx.author.id == filipe:
                    cont = 0
                    cursor.execute("select * from players where nome_player='Filipe'")
                    linha = cursor.fetchone()
                    for i in linha:
                        print(f'{desc[cont]} {i}')
                        result += f'{desc[cont]} {i}\n'
                        cont += 1
                
        if ctx.author.id == malcolm:
                    cont = 0
                    cursor.execute("select * from players where nome_player='Malcolm'")
                    linha = cursor.fetchone()
                    for i in linha:
                        print(f'{desc[cont]} {i}')
                        cont += 1


    #COMANDOS PARA ATUALIZAR

    @commands.command('+vida')
    async def banco(self, ctx, args, dado):
        if args == 'Maze':

            cursor.execute("select vida_max from players where nome_player='Rafa';")
            linha = cursor.fetchone()
            for i in linha:
                vidaTotal = i

            cursor.execute("select vida_atual from players where nome_player='Rafa';")
            linha = cursor.fetchone()
            for i in linha:
                vidaAtual = i
            
            vidaTotal = int(vidaTotal)
            vidaAtual = int(vidaAtual)

            num2 = dado[2:]
            num1 = dado[0]
            num2 = int(num2)
            num1 = int(num1)
            resultMais = 0

            for i in range (0, num1):
                num = randint(1, num2)
                resultMais += num

            if resultMais + vidaAtual > vidaTotal:
                vidaAtual = vidaTotal
                cursor.execute(f"UPDATE players SET vida_atual='{vidaAtual} 'WHERE nome='Maze';")
                con.commit()

                await ctx.send('Vida TOTALMENTE recuperada!')

            else:
                vidaAtual += resultMais
                cursor.execute(f"UPDATE players SET vida_atual='{vidaAtual}' WHERE nome='Maze';")
                con.commit()

                await ctx.send('Vida recuperada!')

            await ctx.reply(f'Total de vida recuperada: {resultMais}')
        
    #COMANDO DE DADOS:

    @commands.command('!d')
    async def dados(self, ctx, args):
        num2 = args[2:]
        num1 = args[0]
        num2 = int(num2)
        num1 = int(num1)
        lista = []
        result = ''

        for i in range (0, num1):
            lista.append(randint(1, num2))
            num = lista[i]
            num = str(num)
            result += ', '+num

        await ctx.reply(f'Resultado: {result}')

def setup(bot):
    bot.add_cog(Rpg(bot))