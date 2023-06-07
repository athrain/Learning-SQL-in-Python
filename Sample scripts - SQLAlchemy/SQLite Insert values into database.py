import sqlite3

connection = sqlite3.connect('../Test databases/kaggle_testset.db')
cursor = connection.cursor()

###insert new value into the DB
#cursor.execute("INSERT INTO Movies VALUES ('Taxi Driver', 'Martin Scorsese','19')")

###adding many values to database
#famousFilms = [('Pulp Fiction', 'Quentin Tarantino', 1994),
               #('Back to the future', 'Steven Spielberg', 1985),
               #('Moonrise Kingdom', 'Wes Anderson', 2012)]

#cursor.executemany('INSERT INTO Movies VALUES (?,?,?)', famousFilms)

###after iteration cursor is empty, so to e.g. use for loop instead we could save the result in records object - not used here
#records = cursor.execute("SELECT * FROM Movies")
#print (cursor.fetchall())

###filtering the data - for the security reason, it should be in tuple
release_year = (1985,)
cursor.execute("SELECT * FROM Movies WHERE year=?", release_year)
print(cursor.fetchall())

connection.commit()
connection.close()