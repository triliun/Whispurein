#Github FileAljabaar
import discord, os, config
from discord.ext import commands
from discord.ext.commands.context import Context
from dotenv import load_dotenv
from events import keep_alive
from module import Myhelper, BanUser, server

Token = os.environ['token']
load_dotenv(".env")
intents = discord.Intents.default()
intents.members = True
intents.presences = True
bot_prefix = "?"
bot = commands.Bot(bot_prefix, intents=intents)

bot.remove_command("help")

bot.lavalink_nodes = [
    {"host": "lavalinkinc.ml", "port": 443, "password": "incognito", "https": True}
]

#isi jika ingin menggunakan spotify
bot.spotify_credentials = {
    "client_id": "CLIENT_ID_HERE",
    "client_secret": "LIENT_SECRET_HERE"
}

@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Game(name=f'{bot_prefix}help | {round(bot.latency * 100)}ms'))
  print(bot.user.id, bot.user.name)
  print("Bot Online")
  
@bot.command()
async def ping(ctx):
  await ctx.send(f':ping_pong:**pong! `{round(bot.latency * 1000)}`ms**')


keep_alive()
bot.add_cog(Myhelper(bot))
bot.add_cog(BanUser(bot))
bot.add_cog(server(bot))
bot.load_extension("dismusic")
bot.load_extension('jishaku')
bot.loop.create_task(on_ready())
bot.run(Token)
