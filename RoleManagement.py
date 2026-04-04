import discord
import os
import random
import time
from datetime import datetime
from dotenv import load_dotenv
from discord.ext import commands
import main



#arrays that are used to categorize roles:
admin = ['Inquisitor','Lexmechanicus (mod team)','Enforcer Primaris','Leadership','Enforcer']
leadership = ['Mission Department Lead','Interrogator','Enforcer Primaris','Inquisitor','Leadership','Team Leader','Tech priest']
detachment = ['Defiance (Armor)','Vengeance (Air)','Harlequin (Actor)', 'Medicae', 'Zeal squad', 'Redemption Squad']
rank = ['Team Leader', 'Squad Leader', 'Trooper', 'Scion', 'Schola', 'Scion', 'Acolyte', 'Agent','Reserves']
department = ['Zeus', 'Archivist','Eden','Enginseer','Harlequin (Actor)']
qualifications = ['BCT','Heavy Weapon: AP','Heavy Weapons: AT', 'Marksmen','Grenadier','Demo','Medical','Vox','Test-Taker']
misc = []
ignored = ['\\\ Other Duties and Titles >>>','<<< Other Game Interests ///', '///Quals>>>', 'new role', '<<< Rank & Detachment ///','Reaction Roles']

'''
A class for role management.

Actions:
Update date with boolean value, if today date has ticked once already, do not update yet, otherwise, begin.
Check all users, if new user, add to db. Check if user is a bot account first.
Check all users roles, if new roles, add to db, if roles do not match current had roles, remove said role!
ignore specific roles.
'''

#cog for role management
class RoleManagement(commands.Cog):
    def __init__(self, user_id, user_name, user_roles=None):
        self.user_id = user_id
        self.user_name = user_name
        self.user_roles = []
        
    #getters
    #setters


'''ROUGH DRAFT OF FUNCTIONS'''


#function for organizing all roles into categories.

async def get_all_roles(ctx, member: discord.Member):
    roles = member.roles
