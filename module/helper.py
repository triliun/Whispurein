import discord
import random
from discord.ext import commands
cmd_prefix = "?"

colors = [0xFFE4E1, 0x00FF7F, 0xD8BFD8, 0xDC143C, 0xFF4500, 0xDEB887, 0xADFF2F, 0x800000, 0x4682B4, 0x006400, 0x808080, 0xA0522D, 0xF08080, 0xC71585, 0xFFB6C1, 0x00CED1]


class Myhelper(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command(name="help")
  async def help(self, ctx):
    em = discord.Embed(
    title='HELP MENU ',
    description="all of my Commands",
    colour = random.choice(colors)
  )
    em.set_thumbnail(url="https://media.discordapp.net/attachments/981125787187036190/1003636464778752041/Whispuere_1.jpg")
    em.set_footer(text=f'- Requested by {ctx.author}', icon_url=ctx.author.avatar_url)
    em.add_field(name='**🎶MUSIC**', value='`play`, `pause`, `resume`, `connect`, `disconnect`, `seek`, `nowplaying`, `queue`, `volume`, `loop`', inline = False)
    em.add_field(name='**❗INFO**', value='`ping`, `server`', inline=False)
    em.add_field(name='**🌕 Prefix**', value=cmd_prefix, inline=False)
    #em.add_field(name = f'{cmd_prefix}stop', value = '`stoped music`',inline = False)
    await ctx.send(embed=em)

print("=====|Checking Commands|=====")
print("By Aljabaar - Github : FileAljabaar")
print("help     =     on")
def setup(bot):
  bot.add_cog(Myhelper(bot))
