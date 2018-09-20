from .story import Story

def setup(bot):
    bot.add_cog(Story(bot))
