import discord
from discord.ext import commands

class BanUser(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    
    @commands.command(pass_context = True)
    async def ban(self, ctx, member:discord.User=None, reason =None):
      if member == None or member == ctx.message.author:
        await ctx.channel.send("You cannot ban yourself")
        return
        if reason == None:
          reason = "Test banh!"
          message = f"You have been banned from {ctx.guild.name} for {reason}"
          await member.send(message)
# await ctx.guild.ban(member, reason=reason)
          await ctx.channel.send(f"{member} is banned!")


print("ban      =     on")
def setup(bot):
  bot.add_cog(BanUser(bot))