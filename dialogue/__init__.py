from .dialogue import Dialogue

def setup(bot):
    bot.add_cog(Dialogue(bot))
