import discord
from discord.ext import commands

import time
import datetime
from datetime import datetime
from datetime import timedelta

startTime = time.time()

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["latency"], description="Shows the ping of the bot")
    async def ping(self, ctx):
        await ctx.message.delete()
        ping = discord.Embed(
            title="",
            color=0x43bab8,
            description=f"🏓 Pong! My ping is **{round(self.bot.latency * 1000)}** ms"
        )
        await ctx.send(embed=ping, delete_after=10)

    @commands.command(description="Shows the bot uptime")
    @commands.is_owner() 
    async def botinfo(self, ctx):
        await ctx.message.delete()
        # Get all users in all servers the bot is in.
        activeServers = self.bot.guilds
        botUsers = 0
        for s in activeServers:
            botUsers += len(s.members)
        # Get the current uptime.
        currentTime = time.time()
        differenceUptime = int(round(currentTime - startTime))
        uptime = str(timedelta(seconds = differenceUptime))
        # Make the embed for the message.
        botinfo = discord.Embed(
            title="Bot info",
            color=0x43bab8,
            timestamp=datetime.now(),
            description=f"**Server Count:** {len(self.bot.guilds)}\n**Bot Users:** {botUsers}\n**Bot Uptime:** {uptime}\n**Ping:** {round(self.bot.latency * 1000)} ms"
        )
        botinfo.set_footer(
            text=f'Requested by {ctx.message.author.name}',
            icon_url=ctx.author.avatar_url
        )
        await ctx.send(embed=botinfo, delete_after=10)

def setup(bot):
    bot.add_cog(Info(bot))