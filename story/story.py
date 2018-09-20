import discord
from redbot.core import commands

class Story:

    def __init__(self, bot):
        self.bot = bot
        self.cont = True

    @commands.group()
    async def story(self, ctx):
        pass

    @story.command()
    async def start(self, ctx):
        """Starts the story of M.O.D.O.K. and Grandmaster"""
        await ctx.send("Story is unavailable at this time.  Please check back later.")

    @story.command()
    async def stop(self, ctx):
        await ctx.send("\n\n**STOPPING**\n\n")
        self.cont = False
        
