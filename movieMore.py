import sqlite3

connection = sqlite3.connect("movie.db")
cursor= connection.cursor()

# cursor.execute('''CREATE TABLE IF NOT EXISTS Movies
#                (Title TEXT, Director TEXT, Yera INT)''' )


# cursor.execute("INSERT INTO Movies VALUES ('Taxi Driver','Martin', 19)") sadece bir sira veri girisi yaptik
# cursor.execute("SELECT * FROM Movies ")

# famousfilms=[("Pulp Fiction","Quantin Tarantino", 1994),("Back To The Future","Steven Spielberg", 1985),
#              ("Moonrise Kingdom","Wes Anderson", 2012)]

# cursor.executemany('INSERT INTO Movies VALUES (?,?,?)', famousfilms) # To insert multiple values.
# records=cursor.execute("SELECT * FROM Movies ")

# print(cursor.fetchall())

# for record in records:
#     print(record)

## Bir onceki kod ile movies db olusturuldu.
releaseyear= (, 1985)

cursor.execute("SELECT * FROM Movies WHERE Yera=?", releaseyear)

print(cursor.fetchall())
connection.commit()
connection.close()

## Simply run the file to create db file we just create.
