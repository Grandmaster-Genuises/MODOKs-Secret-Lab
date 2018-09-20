import discord
from redbot.core import commands
import random

class Dialogue:

    def __init__(self, bot):
        self.bot = bot
        self.insults = ["Kill!!!", "Fry!!!", "Peasant!!!", "Idiot!!!"]

    async def on_message(self, message):
        chance = random.randint(0, 100)

        if chance <= 10:
            await message.channel.send(random.choice(self.insults))
