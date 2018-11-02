import discord
from redbot.core import commands, checks, Config
import random

BaseCog = getattr(commands, "Cog", object)

class Dialogue(BaseCog):

    def __init__(self, bot):
        self.bot = bot
        self.insults = ["Kill!!!", "Fry!!!", "Peasant!!!", "Idiot!!!", "Silence!!!", "Buffoon!!!"]
        self.config = Config.get_conf(self, identifier=2547813692)

        self.config.register_guild(
            active=True,
            chance=10
        )

    async def on_message(self, message):
        if message.author.bot:
            return
        _is_active = await self.config.guild(message.guild).active()
        if _is_active:
            chance = random.randint(0, 100)

            _require = await self.config.guild(message.guild).chance()

            if chance <= _require:
                await message.channel.send(random.choice(self.insults))
        else:
            pass


    @commands.group()
    async def dialogue(self, ctx):
        """Group command for controlling dialogue by MODOK"""
        pass

    @dialogue.command()
    @checks.admin_or_permissions(manage_server=True)
    async def allow(self, ctx, _tf: bool):
        await self.config.guild(ctx.guild).active.set(_tf)
        await ctx.send(f"Dialogue active: {_tf}")

    @dialogue.command()
    @checks.admin_or_permissions(manage_server=True)
    async def chance(self, ctx, _chance: int):
        _is_active = await self.config.guild(ctx.guild).active()
        if not _is_active:
            await ctx.send("Dialogue is not active")
            return
        await self.config.guild(ctx.guild).chance.set(_chance)
        await ctx.send(f"Chance has been set to: {_chance}")

    @dialogue.command()
    async def info(self, ctx):
        _active = await self.config.guild(ctx.guild).active()
        if not _active:
            await ctx.send("Dialogue is not active")
            return
        _chance = await self.config.guild(ctx.guild).chance()
        await ctx.send(f"Dialogue is active\nChance is {_chance}")
        
