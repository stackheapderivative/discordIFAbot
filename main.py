import discord
import os
import random
import time
import database
from datetime import datetime, timezone, time
from dotenv import load_dotenv
from discord.ext import commands, tasks


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

#organization arrays
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
ignored = ['\\\\\\ Other Duties and Titles >>>','<<< Other Game Interests ///', '///Quals>>>', 'new role', '<<< Rank & Detachment ///','Reaction Roles']

#date of today
time = datetime.time(hour=24, minute=0, tzinfo=datetime.UTC) #lets us run the data ingestion every 24 hours.
       
# @client.command()
# async def test_users(ctx):
#     for u in ctx.guild.members: #gets users in the guild
#         usernamesArr.append([u.name]) #gets username
#         discordIDarr.append([u.id]) #gets discord id
#         dateJoinedArr.append([u.joined_at.strftime('%d-%m-%Y')]) #gets datetime of when user joined
#         for r in ctx.guild.roles: #gets the roles of users
#             if r in u.roles and r.name != '@everyone':
#                 rolesArr.append([r.name])
#     await ctx.send(f'TEST COMMAND:\nUSERS:{usernamesArr}\nID:{discordIDarr}\nJOINED:{dateJoinedArr}\nROLES:{rolesArr}\n')


#Class for the ingestion of users and future interactions with users
class UserData(commands.Cog):
    def __init__(self):
        pass

    @client.command()
    async def test_users(self, ctx):
        for u in ctx.guild.members: #gets users in the guild
            usernamesArr.append([u.name]) #gets username
            discordIDarr.append([u.id]) #gets discord id
            dateJoinedArr.append([u.joined_at.strftime('%d-%m-%Y')]) #gets datetime of when user joined
            for r in ctx.guild.roles: #gets the roles of users
                if r in u.roles and r.name != '@everyone':
                    rolesArr.append([r.name])
        await ctx.send(f'TEST COMMAND:\nUSERS:{usernamesArr}\nID:{discordIDarr}\nJOINED:{dateJoinedArr}\nROLES:{rolesArr}\n')

    @tasks.loop(time=time)
    async def ingest_data(self, ctx):
        for u in ctx.guild.members: #gets users in the guild
            usernamesArr.append([u.name]) #gets username
            discordIDarr.append([u.id]) #gets discord id
            dateJoinedArr.append([u.joined_at.strftime('%d-%m-%Y')]) #gets datetime of when user joined
        for r in ctx.guild.roles: #gets the roles of users
            if r in u.roles and r.name != '@everyone':
                rolesArr.append([r.name])
        #FIXME: Add functionalities to organize data here, maybe call a real command that isn't a client.command
        #which can organize the data into the sql database.





if __name__ == "__main__":
    client.run(token)