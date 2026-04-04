import discord
import os
import random
import time
from datetime import datetime
from dotenv import load_dotenv
from discord.ext import commands


#get token
load_dotenv()
intents = discord.Intents.default()

#intents section
intents.message_content = True
client = commands.Bot(command_prefix="?", intents=intents)
token = os.getenv('TOKEN')


#initialize bot
@client.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))

@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    print(f'Message {user_message} by {username} on {channel} at {datetime.now()}')

    if message.author == client.user:
        return

    if channel == "output":
        if user_message.lower() == "help" or user_message.lower() == "hi":
            await message.channel.send(f'Hello {username}. Here are my current commands!\n ?roleget, ?ping, ?announcement...')
            return
        elif user_message.lower() == "67":
            await message.channel.send(f'Get help, {username}')
    await client.process_commands(message) #tells bot to check for defined command

#discord commands

@client.command()
async def ping(ctx):
    if str(ctx.channel.name) == "output":
        await ctx.send('Wanker')
    else:
        await ctx.send('Pong lol!')

@client.command()
async def roleget(ctx, member: discord.Member):
    roles = member.roles #get roles of member
    role_names = [role.name for role in roles if role.name != "@everyone"] #extract role names
    await ctx.send(f"{member.name}'s roles: {','.join(role_names)}")


@client.command()
async def announcement(ctx, message):
    user_message = str(message.content)
    await ctx.send('THIS IS A TEST\n')
    await ctx.send(f'[ANNOUNCEMENT]:\n{user_message}')
    

if __name__ == "__main__":
    client.run(token)