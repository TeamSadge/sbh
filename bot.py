import discord
from discord.ext import commands, tasks
import discord.ext.commands

import os
import json
import datetime
import threading

with open("config.json", "r") as f:
    config = json.load(f)
    
bot = commands.Bot(
    command_prefix = config["prefix"]
)

@bot.event
async def on_ready():
    print("Bot has logged in as {0.user}".format(bot))

for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"cogs.{name}")


@tasks.loop(seconds = 1)
async def checkTime():
    now = datetime.datetime.now()

    current_time = now.strftime("%H:%M:%S") # Returns the time 24-hour format
    print("Current Time =", current_time)

    # if(current_time == "01:29:00"):  # Create channels at 12:50 AM
        # await createChannels()


    # if (current_time == "01:29:10"):  # Delete channels before 5 AM
        # await deleteChannels()

    
# async def createChannels():
#     for guild in bot.guilds:
#         cat = await guild.create_category(config["category_title"])
#         sad_boi_categories[guild.id] = cat
#         await guild.create_text_channel(config["text_channel_title"], category=cat)
#         await guild.create_voice_channel(config["voice_channel_title"], category=cat)


# async def deleteChannels():
#     for guild in bot.guilds:
#         cat = sad_boi_categories[guild.id]
#         if (cat):
#             for channel in cat.channels:
#                 await channel.delete()
#             await cat.delete()

try:
    checkTime.start()
    bot.run(config["token"])
except Exception as err:
    print(f"Error: {err}")