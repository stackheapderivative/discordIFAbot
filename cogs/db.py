import sqlite3


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
    for m in r.values(): #accesses for roles 
        cur.execute('INSERT OR REPLACE INTO Roles (role_name, role_type) VALUES (?,?)', (m['role_name'],m['type']))
        role_id = cur.lastrowid
        role_dict.update({m['role_name']: role_id})
    for i in u.values():
        #accessed the first part of the dict of Users
        cur.execute('INSERT OR REPLACE INTO Users (discord_id, username, date_joined) VALUES (?, ?, ?)', (i['disc_id'],i['name'],i['date']))
        current_user_id = cur.lastrowid
        for j in i['roles']: #NOTE: access roles (a huge list... of lists, each individual role being in a self-contained list. due to zip.
            for z in j: #access the roles individually
                current_role_id = role_dict.get(z) #using get so it returns None, instead of crashing if z is not in there.
                if current_role_id is not None:
                    cur.execute('INSERT OR REPLACE INTO UserRoles (user_id, role_id, role_name) VALUES (?,?,?)', (current_user_id,current_role_id,z))
                else:
                    print(f'ERROR: current_role_id not found! {current_role_id}')
                    print(f'{z} vs {role_dict.get(z)}')

    con.commit()


    #test
    cur.execute('SELECT * From Users')
    cur.execute('SELECT * From Roles')
    cur.execute('SELECT * From UserRoles')
    con.close()


'''
NOTE TO SELF:
    HELLO ME! NOTICE YOU HAD TO GET HELP WITH FIXING THESE ISSUES DUE TO HOW DICTS WORK.
    WE CHANGED R TO R.VALUES() AS THEN WE WOULD BE ACCESSING STILL AN ENTIRE DICT AND HAD ISSUES WITH THAT.
    DUE TO CHANGING IT TO R.VALUES R{} = {M}, WE ARE NOW ABLE TO CALL IT LIKE BEFORE, M[X], M[Z].

    1. DICT:
        FOR KEY IN DICT: ONLY GIVES THE KEYS OR NAMES OF THE ENTRY
        FOR KEY IN DICT.VALUES GIVES US THE ACTUAL DATA. BECAUSE REMEMBER, WE FORMATTED IT AS {KEY{NAME, VALUE}}.

    2. SQLITE:
        WRAP VALUES SENT IN PARATHENSES BECAUSE THAT IS WHAT IS EXPECTED.
    3. DICT LOOKUPS:
        USE DICT[KEY] OR DICT.GET(KEY) , BECAUSE WHEN I TRIED .VALUES() OR .KEYS() WITHOUT FACT CHECKING, THEY RETURN
        ALL VALUES OF SUCH.
    
    THESE ARE NOTES FOR ME TO REVIEW LATER, THEY WILL BE REMOVED.
    '''

'''
    NOTE FOR TESTING:
    do these for testing before moving onto google spreadsheets:
    1. count check, if 3 users, make sure its only 3. same with roles.
    
    2. link test, check a user and see if their things are actually linked.
        select Users.username, Roles.role_name from UserRoles JOIN Users ON UserRoles.user_id = Users.user_id
        JOIN Roles ON UserRoles.role_id = Roles.role_id WHERE Users.username = 'plingplong'
         MUST RETURN SOMETHING LIKE BCT OR ZEUSY
         
    3. Ghost check, look for rows where role_id is null or user_id is null in UserRoles, just in case.
    
    4. Print the entire tables.
    
    Then we move onto printing onto a spreadsheet!!!! :)) WE'RE HALFWAY THERE WOOOOHOOOOO'''