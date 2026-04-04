import discord
from discord.ext import commands, tasks
from datetime import datetime, time

looptime = time(hour=0, minute=0) #lets us run the data ingestion every 24 hours.

#arrays that are used to categorize roles:
admin = ['Inquisitor','Lexmechanicus (mod team)','Enforcer Primaris','Leadership','Enforcer']
leadership = ['Mission Department Lead','Interrogator','Enforcer Primaris','Inquisitor','Leadership','Team Leader','Tech priest']
detachment = ['Defiance (Armor)','Vengeance (Air)','Harlequin (Actor)', 'Medicae', 'Zeal squad', 'Redemption Squad']
rank = ['Team Leader', 'Squad Leader', 'Trooper', 'Scion', 'Schola', 'Scion', 'Acolyte', 'Agent','Reserves']
department = ['Zeus', 'Archivist','Eden','Enginseer','Harlequin (Actor)']
qualifications = ['BCT','Heavy Weapon: AP','Heavy Weapons: AT', 'Marksmen','Grenadier','Demo','Medical','Vox','Test-Taker']
misc = []
ignored = ['\\\\\\ Other Duties and Titles >>>','<<< Other Game Interests ///', '///Quals>>>', 'new role', '<<< Rank & Detachment ///','Reaction Roles']


class UserData(commands.Cog):
    def __init__(self, client):
        self.client = client
        #organization arrays
        self.discordIDarr = []
        self.usernamesArr = []
        self.dateJoinedArr = []
        self.rolesArr = []
        #date of today
        

    #initialize bot
    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(activity=discord.Game("Online for testing!"))
        print('IFA Bot is operational!')

    #Test command for ingesting user data
    @commands.command()
    async def test_users(self, ctx):
        for u in ctx.guild.members: #gets users in the guild
            self.usernamesArr.append([u.name]) #gets username
            self.discordIDarr.append([u.id]) #gets discord id
            self.dateJoinedArr.append([u.joined_at.strftime('%d-%m-%Y')]) #gets datetime of when user joined
            for r in ctx.guild.roles: #gets the roles of users
                if r in u.roles and r.name != '@everyone':
                    self.rolesArr.append([r.name])
        await ctx.send(f'TEST COMMAND:\nUSERS:{self.usernamesArr}\nID:{self.discordIDarr}\nJOINED:{self.dateJoinedArr}\nROLES:{self.rolesArr}\n')

    #Scheduled event for ingesting data and sending to the sql database.
    @tasks.loop(time=looptime)
    async def ingest_data(self, ctx):
        for u in ctx.guild.members: #gets users in the guild
            self.usernamesArr.append([u.name]) #gets username
            self.discordIDarr.append([u.id]) #gets discord id
            self.dateJoinedArr.append([u.joined_at.strftime('%d-%m-%Y')]) #gets datetime of when user joined
        for r in ctx.guild.roles: #gets the roles of users
            if r in u.roles and r.name != '@everyone':
                self.rolesArr.append([r.name])
    
    def organize_data(self, discordIDarr,usernamesArr,rolesArr,dateJoinedArr):
        pass


async def setup(client):
    await client.add_cog(UserData(client))