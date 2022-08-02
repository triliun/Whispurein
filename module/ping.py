import discord
from discord.ext import commands


class Myping(commands.Cog):

  def __init__(self, bot):
   self.bot = bot


print("ping = on")
def setup(bot):
  bot.add_cog(Myping(bot))