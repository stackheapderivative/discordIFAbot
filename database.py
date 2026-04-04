import pymysql


#create db/check if it exists
def db_operation_run():
    

    conn = pymysql.connect(
        host="localhost",
        user="temp",
        password="temp123"
    )
    cur = conn.cursor()
    cur.execute("create database if not exists DISCORD_IFA;") #creates if db not made
    cur.execute("USE DISCORD_IFA;")


    #create values of the table
    create_table_users = (
        "create table if not exists Users("
        "user_id int auto_increment primary key,"
        "discord_id bigint unsigned not null unique,"
        "username varchar(100) not null,"
        "date_joined date not null"
        ");"
    )

    create_table_roles = (
        "create table if not exists Roles("
        "role_id int auto_increment primary key,"
        "role_name varchar(100) not null,"
        "role_type varchar(20) not null,"
        ");"
    )

    create_table_userroles = (
        "create table if not exsits UserRoles("
        "user_id int auto_increment,"
        "role_id int auto increment,"
        "date_assigned date not null,"
        "primary key (user_id, role_id),"
        "foreign key (user_id) references Users(user_id),"
        "foreign key (role_id) references Roles(role_id)"
        ");"
    )

    #commits changes
    conn.commit()
    conn.close()



if __name__ == '__main__':
    db_operation_run()
