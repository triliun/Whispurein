import discord
import random
from discord.ext import commands
cmd_prefix = "?"

colors = [0xFFE4E1, 0x00FF7F, 0xD8BFD8, 0xDC143C, 0xFF4500, 0xDEB887, 0xADFF2F, 0x800000, 0x4682B4, 0x006400, 0x808080, 0xA0522D, 0xF08080, 0xC71585, 0xFFB6C1, 0x00CED1]


class server(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command(name="server")
  async def server(self, ctx):
    em = discord.Embed(
    title=f'**{ctx.guild.name} INFO**',
    colour = random.choice(colors)
  )
    em.set_footer(text=f'- Requested by {ctx.author}', icon_url=ctx.author.avatar_url)
    em.add_field(name='**🆔 Server ID :**', value=f'{ctx.guild.id}', inline = False)
    em.add_field(name='**📆 Created On :**', value=f'`{ctx.guild.created_at.strftime("%b %d %Y")}`', inline=False)
    em.add_field(name='**👑 Owner By :**', value=f'<@{ctx.guild.owner.id}>', inline=False)
    em.add_field(name=f'**👥 Members**', value =f'{ctx.guild.member_count} members', inline=False)
    em.add_field(name='**💬 Channels**', value=f'{len(ctx.guild.text_channels)} Text | {len(ctx.guild.voice_channels)} Voice', inline=False)
    em.add_field(name='**🌎 Region :**', value=f'{ctx.guild.region}', inline=False)
    em.add_field(name=f'**🌟 Roles ({len(ctx.message.guild.roles)})**', value=f'***use ?role to more informations***', inline=False)
    #em.set_author(name=f'{ctx.guild.name}', icon_url=ctx.guild.icon_url)
    #em.add_field(name = f'', value = '',inline = False)
    await ctx.send(embed=em)


print("help     =     on")
def setup(bot):
  bot.add_cog(server(bot))