import discord
from discord.ext import commands, tasks
from datetime import datetime, time
import db
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


#NOTE: DUMMY ARRAYS
test_admin = ['Not inquisitor']
test_leadership = ['Blundership']
test_detachment = ['Zeal?!??!']
test_rank = ['Schola','Silly']
test_department = ['Zeusy','Edener']
test_qualifications = ['BCT','Demo','Medical','Vox']
test_misc = []
test_ignored = ['<<< Rank & Detachment ///','<<< Other Game Interests ///','\\\\\\ Other Duties and Titles >>>','///Quals >>>','John The Servitor']

#dictionaries for data organization
Users = {}
Roles = {}
class UserData(commands.Cog):
    def __init__(self, client):
        self.client = client
        #organization arrays
        self.discordIDarr = []
        self.usernamesArr = []
        self.dateJoinedArr = []
        self.rolesArr = []
        self.temp_rolesArr = []
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
                if r in u.roles and r.name != '@everyone' and r.name not in test_ignored and r.name not in self.temp_rolesArr:
                    self.temp_rolesArr.append([r.name]) #temp is used to store temporarily for one user, store as list in roles.
            self.rolesArr.append([self.temp_rolesArr])
        # await ctx.send(f'TEST COMMAND:\nUSERS:{self.usernamesArr}\nID:{self.discordIDarr}\nJOINED:{self.dateJoinedArr}\nROLES:{self.rolesArr}\n')
        #FIXME: TEST
        # testobj = list(zip(self.usernamesArr, self.rolesArr))
        # for i in testobj:
        #     await ctx.send(f'TEST: {i}')
        self.organize_data()

    #Scheduled event for ingesting data and sending to the sql database.
    @tasks.loop(time=looptime)
    async def ingest_data(self, ctx):
        for u in ctx.guild.members: #gets users in the guild
            self.usernamesArr.append([u.name]) #gets username
            self.discordIDarr.append([u.id]) #gets discord id
            self.dateJoinedArr.append([u.joined_at.strftime('%d-%m-%Y')]) #gets datetime of when user joined
            for r in ctx.guild.roles: #gets the roles of users
                if r in u.roles and r.name != '@everyone' and r.name not in test_ignored:
                    self.temp_rolesArr.append([r.name])
            self.rolesArr.append([self.temp_rolesArr])
    
    def organize_data(self):
        #loop for user information
        user_information = zip(self.usernamesArr, self.discordIDarr, self.dateJoinedArr, self.rolesArr)
        for i in user_information:
            Users.update({i[0][0]:{'name':i[0][0],'disc_id':i[1][0],'date':i[2][0], 'roles':i[3][0]}})
        #FIXME: TEST USERS
        print(Users)
        for l in self.temp_rolesArr:
            for i in l:
                if i in test_admin:
                    Roles.update({i:{'role_name':i,'type':0}})
                elif i in test_leadership:
                    Roles.update({i:{'role_name':i,'type':1}})
                elif i in test_detachment:
                    Roles.update({i:{'role_name':i,'type':2}})
                elif i in test_rank:
                    Roles.update({i:{'role_name':i,'type':3}})
                elif i in test_department:
                    Roles.update({i:{'role_name':i,'type':4}})
                elif i in test_qualifications:
                    Roles.update({i:{'role_name':i,'type':5}})
                else:
                    Roles.update({i:{'role_name':i,'type':6}})
        #FIXME: TEST ROLES
        print(Roles)
        db.populate(Users,Roles) #sends data to sqlite3








async def setup(client):
    await client.add_cog(UserData(client))