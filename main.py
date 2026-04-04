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
intents.members = True


#intents section
intents.message_content = True
client = commands.Bot(command_prefix="?", intents=intents)
token = os.getenv('TOKEN')


#initialize bot
@client.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))

'''
get users information, such as name, id, and roles.
'''

#test arrays
discordIDarr = []
usernamesArr = []
dateJoinedArr = []
rolesArr = []

#arrays that are used to categorize roles:
admin = ['Inquisitor','Lexmechanicus (mod team)','Enforcer Primaris','Leadership','Enforcer']
leadership = ['Mission Department Lead','Interrogator','Enforcer Primaris','Inquisitor','Leadership','Team Leader','Tech priest']
detachment = ['Defiance (Armor)','Vengeance (Air)','Harlequin (Actor)', 'Medicae', 'Zeal squad', 'Redemption Squad']
rank = ['Team Leader', 'Squad Leader', 'Trooper', 'Scion', 'Schola', 'Scion', 'Acolyte', 'Agent','Reserves']
department = ['Zeus', 'Archivist','Eden','Enginseer','Harlequin (Actor)']
qualifications = ['BCT','Heavy Weapon: AP','Heavy Weapons: AT', 'Marksmen','Grenadier','Demo','Medical','Vox','Test-Taker']
misc = []
#ignored = ['\\\ Other Duties and Titles >>>','<<< Other Game Interests ///', '///Quals>>>', 'new role', '<<< Rank & Detachment ///','Reaction Roles']

@client.command()
async def test_users_and_roles(ctx):
        for n in ctx.guild.members:
             usernamesArr.append(n.name)
        for r in ctx.guild.roles:
             if r.name == '@everyone':
                  pass
             else:
                rolesArr.append(r.name)
        await ctx.send(f'TEST COMMAND:\n{usernamesArr}\n{rolesArr}')
        
@client.command()
async def test_users(ctx):
    for u in ctx.guild.members: #gets users in the guild
        usernamesArr.append([u.name]) #gets username
        discordIDarr.append([u.id]) #gets discord id
        dateJoinedArr.append([u.joined_at.strftime('%d-%m-%Y')]) #gets datetime of when user joined
        for r in ctx.guild.roles: #gets the roles of users
            if r in u.roles and r.name != '@everyone':
                rolesArr.append([r.name])
    await ctx.send(f'TEST COMMAND:\nUSERS:{usernamesArr}\nID:{discordIDarr}\nJOINED:{dateJoinedArr}\nROLES:{rolesArr}\n')

if __name__ == "__main__":
    client.run(token)