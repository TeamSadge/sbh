import discord
from discord.ext import commands

import json
import datetime
from datetime import date
from datetime import datetime
import asyncio
import os.path
from time import localtime

class Setup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def setup(self, ctx, *, arg=""):
        gid = ctx.guild.id
        guildName = ctx.guild.name
        fpath = f"./data/{gid}.json"
        
        if (os.path.isfile(fpath)):
            with open(fpath, "r") as file:
                data = json.load(file)
                await ctx.send(f'```json\n${data}\n```')
        else:
            data = {
                "gid": gid,
                "name": guildName,
                "start_time": "01:00:00",
                "end_time": "04:59:59",
                "catagory_name": "sad boi hours",
                "tchannel_name": "sad boi hours",
                "vchannel_name": "sad boi hours"
            }
            with open(fpath, "w") as file:
                json.dump(data, file, indent=4)

            await ctx.message.delete()
            errorEmbed = discord.Embed(
                color=0xff4f4f
            )
    
def setup(bot):
    bot.add_cog(Setup(bot))

