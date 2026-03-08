import discord
import discord
import random
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

@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')

@bot.command()
async def dado(ctx):
    numero = random.randint(1, 6)
    await ctx.send(f"🎲 Salió: {numero}")
@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def img_random(ctx):
    os.system("cls")

    # rarezas y probabilidades
    rarezas = ["comun", "poco_comun"]
    probabilidades = [80, 20]

    rareza = random.choices(rarezas, probabilidades)[0]

    ruta = f'imagenes/{rareza}'
    lista_archivos = os.listdir(ruta)
    img_name = random.choice(lista_archivos)

    with open(f'{ruta}/{img_name}', 'rb') as f:
        picture = discord.File(f)

    await ctx.send(f"🎲 Rareza: **{rareza}**")
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
    
bot.run("TOKEN")


