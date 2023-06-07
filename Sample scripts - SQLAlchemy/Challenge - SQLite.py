import sqlite3

###CHALLENGE
###Create a table Users with Id, First name, Last name, Email (two of them with Gmail) and then print email column only

###create database based on kaggle dataset - as it's first time we create such database, it creates it. Aftewards, it will just connect to that db.
connection = sqlite3.connect('../Test databases/challenge_1.db')

cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Users
               (User_ID TEXT, First Name TEXT, Last Name TEXT, Email Address TEXT)''')


###adding many values to database
usersGroup = [('1', 'Danny', "Devito", '''hfsg.uihddu@gmail.com'''),
            ('2', 'Emma', "Devito", '''ysahgdy.jhsdya@gmail.com'''),
            ('3', 'Harry', "Devato", '''hfsg.uihddu@asdasd.com'''),
            ('4', 'Ginger', "Devito", '''hfsg.uihddu@uyas.com'''),
            ('5', 'Bread', "Devito", '''hfsg.uihddu@ihjhnsd.com''')]

cursor.executemany('INSERT INTO Users VALUES (?,?,?,?)', usersGroup)

records = cursor.execute("SELECT Email Address FROM Users")
print (cursor.fetchall())

connection.commit()
connection.close()