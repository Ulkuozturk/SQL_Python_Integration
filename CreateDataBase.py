import sqlite3

connection = sqlite3.connect('users-sqlite.db')

cursor= connection.cursor()

cursor.execute(''' CREATE TABLE IF NOT EXISTS Users
               (user_id INTEGER PRIMARY KEY AUTOINCREMENT, first_name TEXT,
               last_name TEXT,
               email_address TEXT)
               ''')

usersToInsert=[('Tina','Meccoy', 'tnns@sada'),
               ('Joan','ssds','asdasd@grg'),
               ('Sara','Cox','erSara@kekd'),
               ('Jessica','Alvarez','asfasdf@weq')]
cursor.executemany('''  
                   INSERT INTO Users(first_name, last_name, email_address)
                   VALUES (?,?,?)
                   ''', usersToInsert)

cursor.execute("SELECT email_address FROM Users")
print(cursor.fetchall())

cursor.execute("SELECT * FROM Users")
print(cursor.fetchall())

connection.commit()
connection.close()
