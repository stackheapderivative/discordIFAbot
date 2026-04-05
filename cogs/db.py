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
                FOREIGN KEY(user_id) references Users(user_id),
                FOREIGN KEY (role_id references Roles(role_id)
                )''')
    


    con.commit()
    con.close()

def populate(u, r):
    con = sqlite3.connect('IFA.db')
    cur = con.cursor()
    for i in r:
        cur.execute('INSERT INTO Roles (role_name, role_type) VALUES (?,?)', i['role_name'],i['type'])
    for i in u:
        #accessed the first part of the dict
        cur.execute('INSERT INTO Users (discord_id, username, date_joined) VALUES (?, ?, ?)', i['disc_id'],i['name'],i['date'])
        for j in u['roles']: #access roles
            for z in j: #access the roles individually
                cur.execute('INSERT INTO UserRoles (role_name) VALUES (?)', i['roles'])
                



                
                    