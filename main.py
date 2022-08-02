#Github FileAljabaar
import discord, os
from discord.ext import commands
from discord.ext.commands.context import Context
from dotenv import load_dotenv
from events import keep_alive
from module import Myhelper, BanUser

Token = os.environ['token']
load_dotenv(".env")

bot_prefix = "?"
bot = commands.Bot(bot_prefix)

bot.remove_command("help")

bot.lavalink_nodes = [
    {"host": "lavalinkinc.ml", "port": 443, "password": "incognito", "https": True}
]

#isi jika ingin menggunakan spotify
bot.spotify_credentials = {
    "client_id": "CLIENT_ID_HERE",
    "client_secret": "LIENT_SECRET_HERE",
}
 
@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Game(name=f'whispurein.io | {bot_prefix}help'))
  print("Bot Online")

@bot.command()
async def ping(ctx):
  await ctx.send(f'pong! `{round(bot.latency * 1000)}ms`')


keep_alive()
bot.add_cog(Myhelper(bot))
bot.add_cog(BanUser(bot))
#bot.add_cog(Myping(bot))
bot.load_extension("dismusic")
bot.load_extension('jishaku')
bot.run(Token)