import discord
import os
import random
import db
from dotenv import load_dotenv
from discord.ext import commands, tasks
from cogs.UserData import UserData #cog for handling user data

'''
Client class:
This class is used to start the bot and load all cogs the bot requires.
The reason for this usage is due to how OOPified discordpy was since 2.0, therefore, cannot load cogs without async.
'''
class Client(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default() #intents
        intents.message_content = True #allow bot to read msgs
        intents.members = True #allow bot to do member events
        super().__init__(command_prefix="?", intents=intents)

    #runs automatically before bot starts to load in cogs
    async def setup_hook(self):
        print('Running setup hook......')
        await self.load_extension("cogs.UserData")

if __name__ == "__main__":
    client = Client()
    load_dotenv() #get token
    token = os.getenv('TOKEN')
    client.run(token)
