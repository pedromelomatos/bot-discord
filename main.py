import discord
from discord.ext import commands
from infos import token

intents = discord.Intents.all() #permissões do discord salvadas em uma variável, nesse caso as permissões que o nosso bot tem são todas.

bot = commands.Bot(".", intents=intents) # uma variável representando nosso bot. "." é o prefixo que o bot vai usar para identificar comandos. Por exemplo, se tiver um comando chamado ping, é pra chamar ele assim no Discord: .ping. E o intents é só falando que as permissões que o nosso bot vai ter são as que a gente armazenou na variável intents.

@bot.event
async def on_ready():
    print(f"{'=-'*20}\nBot inicializado com sucesso.\n{'=-'*20}")

@bot.command()
async def ola(ctx):
    await ctx.reply("Olá, sou o Rafinha como posso te ajudar? ")


bot.run(f"{token}") #"roda esse bot dessa token"