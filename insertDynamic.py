import psycopg2
def insert_incident(conn,i,Date,Ship_Type,Lat1,Lon1,Piracy_Area,Ship_Name,Location):
    piracy_data=(i,Date,Ship_Type,Lat1,Lon1,Piracy_Area,Ship_Name,Location)
    cur=conn.cursor()
    cur.execute('''
                INSERT INTO piracy(i,Date,Ship_Type,Lat1,Lon1,Piracy_Area,Ship_Name,
                Location) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)''', piracy_data)
    conn.commit()
    cur.execute(''' 
                SELECT Lat1, Lon1, Piracy_Area FROM piracy WHERE Ship_Type=%s;
                ''', (Ship_Type,))

    rows=cur.fetchall()
    for row in rows:
        print(row)
    
if __name__ == '__main__':    
    conn= psycopg2.connect(database= "postgres",
                 user = "postgres",
                 password = "Dea123456",
                 host = "localhost",
                 port = "5432")

    Ship_Type = input("What is the type of the ship \n")
    Date    =  input("What is the Date of incident \n")
    Lat1    = input("What is the latitude of incident \n")           
    Lon1    = input("What is the longitude of incident \n")
    Piracy_Area = input("What is area of incident \n")
    Ship_Name = input("What is the name of ship \n")
    Location = input("What is the Location \n")
    i = input("What is the primary key \n")
    
    insert_incident(conn,i,Date,
                Ship_Type,
                Lat1,
                Lon1,
                Piracy_Area,
                Ship_Name,
                Location)
    conn.close()