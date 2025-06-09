import discord
from discord.ext import commands
from infos import token

intents = discord.Intents.all() 

#permissões do discord salvadas em uma variável, nesse caso as permissões que o nosso bot tem são todas.

bot = commands.Bot(".", intents=intents) 

# uma variável representando nosso bot. "." é o prefixo que o bot vai usar para identificar comandos. Por exemplo, se tiver um comando chamado ping, é pra chamar ele assim no Discord: .ping. E o intents é só falando que as permissões que o nosso bot vai ter são as que a gente armazenou na variável intents.

@bot.event
async def on_ready():
    print(f"{'=-'*20}\nBot inicializado com sucesso.\n{'=-'*20}")

@bot.command()
async def ola(ctx:commands.Context):
    usuario = ctx.author.display_name
    await ctx.reply(f"Olá {usuario}, sou o Rafinha como posso te ajudar? ")

@bot.command()
async def nome(ctx:commands.Context, nome, sobrenome):
    await ctx.reply(f"Seu nome é {nome} e seu sobrenome é {sobrenome}?")

#ctx aqui de parâmetro é literalmente o contexto em qual a função está sendo chamada (servidor, canal de texto específico, etc)

#os parametros são as palavras que o usuário digita em ordem 

bot.run(f"{token}") #"roda esse bot dessa token"