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

# o nome das nossas funções de eventos é padronizado pelo oq o discord já nos disponibiliza

@bot.event
async def on_message(msg:discord.Message):
    if msg.content == 'Rafinha':
        await msg.reply('Rafinha sou eu. Se tiver com dúvidas sobre como posso te ajudar digite `.comandos` =)')
        await bot.process_commands(msg) 
    await bot.process_commands(msg) #se não for Rafinha a mensagem, processa ela como um comando e vê se ela é um comando.

@bot.event
async def on_member_join(membro:discord.Member):
    canal = bot.get_channel(952211300614815778)
    await canal.send(f"salve {membro.display_name}")

@bot.command()
async def comandos(ctx:commands.Context):
    await ctx.reply("👋 **Oi, eu sou o Rafinha! Aqui estão os meus comandos disponíveis:**\n\n"
        "📌 `.ola`\n"
        "Eu te dou um olá personalizado com seu nome!\n"
        "👉 Exemplo: `.ola`\n\n"
        "📌 `.nome <nome> <sobrenome>`\n"
        "Te digo seu nome completo.\n"
        "👉 Exemplo: `.nome Pedro Silva`\n\n"
        "📌 `.soma <número1> <número2>`\n"
        "Faço uma conta pra você =) \n"
        "👉 Exemplo: `.soma 10 15`\n\n"
        "Se precisar de mim, só chamar. Tamo junto, bigode! 😎")

@bot.command()
async def ola(ctx:commands.Context):
    usuario = ctx.author.display_name
    await ctx.reply(f"Olá {usuario}, sou o Rafinha como posso te ajudar? ")

@bot.command()
async def nome(ctx:commands.Context, nome, sobrenome):
    await ctx.reply(f"Seu nome é {nome} e seu sobrenome é {sobrenome}?")

@bot.command()
async def soma(ctx:commands.Context, num1, num2):
    numero1 = int(num1)
    numero2 = int(num2)
    await ctx.reply(f'A soma de {numero1} com {numero2} é {numero1+ numero2}. Correto?')
 
#ctx aqui de parâmetro é literalmente o contexto em qual a função está sendo chamada (servidor, canal de texto específico, etc)

#os parametros são as palavras que o usuário digita em ordem 

bot.run(f"{token}") #"roda esse bot dessa token"