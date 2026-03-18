import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

touhou6 = {

"reimu": {
"nombre": "Reimu Hakurei",
"descripcion": "Sacerdotisa del Santuario Hakurei.",
"poder": "★★★★★",
"aparicion": "Protagonista jugable",
"tema": "Maiden's Capriccio ~ Dream Battle",
"imagen": "https://en.touhouwiki.net/images/7/7d/Th135Reimu.png",
"spellcards": [
"Fantasy Seal",
"Evil-Sealing Circle"
]
},

"marisa": {
"nombre": "Marisa Kirisame",
"descripcion": "Maga humana experta en magia ofensiva.",
"poder": "★★★★★",
"aparicion": "Protagonista jugable",
"tema": "Love-Colored Magic",
"imagen": "https://en.touhouwiki.net/images/9/9c/Th135Marisa.png",
"spellcards": [
"Master Spark",
"Stardust Reverie"
]
},

"rumia": {
"nombre": "Rumia",
"descripcion": "Youkai que controla la oscuridad.",
"poder": "★☆☆☆☆",
"aparicion": "Stage 1 Boss",
"tema": "Apparitions Stalk the Night",
"imagen": "https://en.touhouwiki.net/images/0/0f/Th06Rumia.png",
"spellcards": [
"Moonlight Ray",
"Night Bird"
]
},

"cirno": {
"nombre": "Cirno",
"descripcion": "Hada de hielo extremadamente confiada.",
"poder": "★★☆☆☆",
"aparicion": "Stage 2 Boss",
"tema": "Beloved Tomboyish Daughter",
"imagen": "https://en.touhouwiki.net/images/6/6c/Th06Cirno.png",
"spellcards": [
"Icicle Fall",
"Perfect Freeze"
]
},

"meiling": {
"nombre": "Hong Meiling",
"descripcion": "Guardiana de la Mansión Scarlet Devil.",
"poder": "★★★☆☆",
"aparicion": "Stage 3 Boss",
"tema": "Shanghai Scarlet Teahouse",
"imagen": "https://en.touhouwiki.net/images/3/3f/Th06Meiling.png",
"spellcards": [
"Colorful Rain",
"Rainbow Wind Chime"
]
},

"patchouli": {
"nombre": "Patchouli Knowledge",
"descripcion": "Hechicera de la biblioteca.",
"poder": "★★★★☆",
"aparicion": "Stage 4 Boss",
"tema": "Voile, the Magic Library",
"imagen": "https://en.touhouwiki.net/images/8/8b/Th06Patchouli.png",
"spellcards": [
"Agni Shine",
"Princess Undine",
"Metal Fatigue"
]
},

"sakuya": {
"nombre": "Sakuya Izayoi",
"descripcion": "Sirvienta que manipula el tiempo.",
"poder": "★★★★☆",
"aparicion": "Stage 5 Boss",
"tema": "Lunar Clock ~ Luna Dial",
"imagen": "https://en.touhouwiki.net/images/0/0c/Th06Sakuya.png",
"spellcards": [
"Killer Doll",
"Perfect Square"
]
},

"remilia": {
"nombre": "Remilia Scarlet",
"descripcion": "Vampiresa dueña de la Mansión Scarlet Devil.",
"poder": "★★★★★",
"aparicion": "Final Boss",
"tema": "Septette for the Dead Princess",
"imagen": "https://en.touhouwiki.net/images/4/4f/Th06Remilia.png",
"spellcards": [
"Scarlet Gensokyo",
"Red Magic: Scarlet Devil"
]
},

"flandre": {
"nombre": "Flandre Scarlet",
"descripcion": "Hermana menor de Remilia, extremadamente peligrosa.",
"poder": "★★★★★",
"aparicion": "Extra Stage Boss",
"tema": "U.N. Owen Was Her?",
"imagen": "https://en.touhouwiki.net/images/5/56/Th06Flandre.png",
"spellcards": [
"Taboo: Cranberry Trap",
"Q.E.D: Ripples of 495 Years"
]
}

}


class PersonajeSelect(discord.ui.Select):

    def __init__(self):

        options = [
            discord.SelectOption(label="Reimu Hakurei", value="reimu"),
            discord.SelectOption(label="Marisa Kirisame", value="marisa"),
            discord.SelectOption(label="Rumia", value="rumia"),
            discord.SelectOption(label="Cirno", value="cirno"),
            discord.SelectOption(label="Hong Meiling", value="meiling"),
            discord.SelectOption(label="Patchouli Knowledge", value="patchouli"),
            discord.SelectOption(label="Sakuya Izayoi", value="sakuya"),
            discord.SelectOption(label="Remilia Scarlet", value="remilia"),
            discord.SelectOption(label="Flandre Scarlet", value="flandre")
        ]

        super().__init__(
            placeholder="Selecciona un personaje de Touhou 6",
            options=options
        )

    async def callback(self, interaction: discord.Interaction):

        personaje = self.values[0]
        datos = touhou6[personaje]

        embed = discord.Embed(
            title=datos["nombre"],
            description=datos["descripcion"],
            color=0xff0000
        )

        embed.add_field(name="⭐ Poder", value=datos["poder"], inline=False)
        embed.add_field(name="🏰 Aparición", value=datos["aparicion"], inline=False)
        embed.add_field(name="🎵 Tema", value=datos["tema"], inline=False)

        spells = "\n".join(datos["spellcards"])
        embed.add_field(name="🎴 Spell Cards", value=spells, inline=False)

        embed.set_image(url=datos["imagen"])

        await interaction.response.send_message(embed=embed)


class PersonajeView(discord.ui.View):

    def __init__(self):
        super().__init__()
        self.add_item(PersonajeSelect())


@bot.command()
async def touhou6(ctx):
    await ctx.send(
        "📖 Enciclopedia Touhou 6\nSelecciona un personaje:",
        view=PersonajeView()
    )


@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")


bot.run("TU_TOKEN_AQUI")
