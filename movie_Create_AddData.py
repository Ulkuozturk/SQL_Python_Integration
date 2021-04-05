import sqlite3

connection = sqlite3.connect("movie.db")
cursor= connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Movies
               (Title TEXT, Director TEXT, Yera INT)''' )

famousfilms=[("Pulp Fiction","Quantin Tarantino", 1994),("Back To The Future","Steven Spielberg", 1985),
             ("Moonrise Kingdom","Wes Anderson", 2012)]

cursor.executemany('INSERT INTO Movies VALUES (?,?,?)', famousfilms) # To insert multiple values.
records=cursor.execute("SELECT * FROM Movies ")

print(cursor.fetchall())

for record in records:
    print(record)
    
connection.commit()
connection.close()

## Simply run the file to create db file we just create.
