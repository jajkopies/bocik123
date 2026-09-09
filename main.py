import discord
from discord.ext import commands
import random
import os

TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

odpowiedzi = {
    "siema": ["elo", "siema", "spierdalaj"],
    "co tam u ciebie": ["git", "spoko", "hujowo"],
    "jebać cię": ["spierdalaj", "twoją mamę"],
    "kocham cię": ["ja ciebie też", "ty geju","nasrałem ci na wycieraczkę"]
}

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Bot {bot.user} online")

@bot.event
async def on_message(message):
    if message.author.bot: return
    if bot.user in message.mentions:
        text = message.content.lower()
        for key, vals in odpowiedzi.items():
            if key in text:
                await message.channel.send(f"{message.author.mention} {random.choice(vals)}")
                break
    await bot.process_commands(message)

@bot.tree.command(name="8ball", description="Magiczna kula 8")
async def eight_ball(interaction: discord.Interaction, pytanie: str):
    opcje = ["tak", "nie", "na pewno", "na 100%", "oczywiście że nie", "może"]
    await interaction.response.send_message(f" {pytanie} -> {random.choice(opcje)}")

bot.run(TOKEN)
