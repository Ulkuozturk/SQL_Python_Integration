import psycopg2

conn= psycopg2.connect(database= "postgres",
                 user = "postgres",
                 password = "password",
                 host = "localhost",
                 port = "5432")

cursor = conn.cursor()

cursor.execute('''
               CREATE TABLE Piracy
               ( i INT PRIMARY KEY,
                Date TEXT,
                Ship_Type TEXT,
                Lat1 REAL,
                Lon1 REAL,
                Piracy_Area TEXT,
                Ship_Name TEXT ,
                Location TEXT);
               ''')

conn.commit()
conn.close()