import psycopg2

conn= psycopg2.connect(database= "postgres",
                 user = "postgres",
                 password = "Dea123456",
                 host = "localhost",
                 port = "5432")

cursor = conn.cursor()


# cursor.execute("SELECT * FROM piracy LIMIT 10")
# print(cursor.fetchall())

# cursor.execute('''
#                INSERT INTO piracy(
#                 i,Date,
#                 Ship_Type,
#                 Lat1,
#                 Lon1,
#                 Piracy_Area,
#                 Ship_Name,
#                 Location
#                ) VALUES (
#                   5003,'2009-01-01','Tanker',12,45,
#                   'Teritorial_Waters',
#                   'Vessel',
#                   'Arabian_Sea'
#                )
#                ''')

# conn.commit()
cursor.execute("SELECT Piracy_Area,Lat1,Lon1 from piracy WHERE Ship_Type='Bulk'")
rows=cursor.fetchall()
for row in rows:
    print(row)
conn.close()