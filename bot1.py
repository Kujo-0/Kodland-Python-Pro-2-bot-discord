import discord
import discord
from discord.ext import commands
from bot_logic import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command(name="mambo")
async def mambo(ctx):
    await ctx.send("mambo")

@bot.command(name="a")
async def mambo(ctx):
    await ctx.send("a")

@bot.command()
async def password(ctx, length: int):
    nueva_pass = gen_pass(length)
    await ctx.send(f" Tu contraseña es:\n`{nueva_pass}`")

@bot.command()
async def dado(ctx):
    numero = random.randint(1, 6)
    await ctx.send(f"🎲 Salió: {numero}")
@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

bot.run("TOKEN")

#no coloco el id del token por las dudas