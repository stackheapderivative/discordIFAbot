import sqlite3
from UserData import UserData

'''
DATA FORMATTING:
FOR USERS TABLE SEND: discord_id, username, date_joined.
FOR ROLES TABLE: send role name, role type.
FOR USERROLES TABLE: send date_assigned, this table is used to link roles to a user.
'''

def operate_db():
    #cursor
    con = sqlite3.connect('IFA.db')
    cur = con.cursor()

    #create user table
    cur.execute('''
                CREATE TABLE IF NOT EXISTS Users (
                user_id INT AUTO_INCREMENT PRIMARY KEY,
                discord_id BIGINT UNSIGNED NOT NULL UNIQUE,
                username VARCHAR(100) NOT NULL,
                date_joined DATE NOT NULL
                )
                ''')
    #create roles table
    cur.execute('''
                CREATE TABLE IF NOT EXISTS Roles(
                role_id INT AUTO_INCREMENT PRIMARY KEY,
                role_name VARCHAR(100) NOT NULL,
                role_type INT NOT NULL
                )''')
    #creates UserRoles table
    cur.execute('''
                CREATE TABLE IF NOT EXISTS UserRoles(
                user_id INT AUTO_INCREMENT,
                role_id int AUTO_INCREMENT,
                role_name VARCHAR(100) NOT NULL,
                PRIMARY KEY(user_id, role_id),
                FOREIGN KEY (user_id) references Users(user_id),
                FOREIGN KEY (role_id) references Roles(role_id)
                )''')
    


    con.commit()
    con.close()

def populate(u, r):
    role_dict = {}
    con = sqlite3.connect('IFA.db')
    cur = con.cursor()
    for m in r: #accesses for roles FIXME: MAKE THIS ITERATE ROLES.VALUES()
        cur.execute('INSERT INTO Roles (role_name, role_type) VALUES (?,?)', m['role_name'],m['type'])
        role_id = cur.lastrowid
        role_dict.update({m['role_name']: role_id})
    for i in u:
        #accessed the first part of the dict of Users
        cur.execute('INSERT INTO Users (discord_id, username, date_joined) VALUES (?, ?, ?)', i['disc_id'],i['name'],i['date'])
        current_user_id = cur.lastrowid
        for j in i['roles']: #NOTE: access roles (a huge list... of lists, each individual role being in a self-contained list. due to zip.
            for z in j: #access the roles individually
                current_role_id = role_dict.get(z) #using get so it returns None, instead of crashing if z is not in there.
                cur.execute('INSERT INTO UserRoles (user_id, role_id, role_name) VALUES (?,?,?)', current_user_id,current_role_id,i['roles'])
                
'''CURRENT ISSUES:
        for i in u, this makes i = "Username", so I will not be able to access anything else. I MUST redit this to look at values, because I forgot how dictionaries work somehow lol
        In roles, '''


                
                    