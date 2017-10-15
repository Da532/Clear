#Clear! by Da532.


#---CONFIG---

token = "TOKEN_HERE" #To find this, press CTRL + SHIFT + i in the Discord client revealing the inspect element prompt. Click the arrows, head over to Application, local storage and there you can find your user token :)

#--- BOT ---

import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix="!", self_bot=True)
bot.remove_command("help")

@bot.event
async def on_ready():
    print ("Ready when you are. ;)") 
    print ("Name: {}".format(bot.user.name))
    print ("ID: {}".format(bot.user.id))

@bot.command(pass_context=True)
async def clear(ctx, limit: int=None):
    async for msg in bot.logs_from(ctx.message.channel, limit=limit):
        if msg.author:
            await bot.delete_message(msg)
    embed = discord.Embed(description="Action completed! :smile:", color=0x00ff00)
    await bot.say (embed=embed)

bot.run(token, bot=False)