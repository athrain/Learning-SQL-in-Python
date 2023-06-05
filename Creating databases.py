###learning how to create databases in Python

import sqlite3

###create database based on kaggle dataset - as it's first time we create such database, it creates it. Aftewards, it will just connect to that db.
connection = sqlite3.connect('kaggle_testset.db')

cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Movies
               (Title TEXT, Director TEXT, Year INT)''')
###SQLite does not have datetime values, only integers

connection.commit()
connection.close()