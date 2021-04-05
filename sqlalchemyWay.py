from sqlalchemy import create_engine, Table, MetaData

engine= create_engine('postgresql://postgres:password@localhost/postgres')

with engine.connect() as connection:
    meta = MetaData(engine)
    Piracy= Table('piracy', meta, autoload=True, autoload_with=engine)
    
    # Create
    insert_statement = Piracy.insert().values(
        i= 7000,
        date= '2009-01-01',
        ship_type='Tanker',
        lat1=12,
        lon1=45,
        piracy_area='Teritorial_Waters',
        ship_name= 'Vessel',
        location= 'Arabian_Sea')
    
    connection.execute(insert_statement)
    
    # Read
    select_statement = Piracy.select().limit(10)
    result_set= connection.execute(select_statement)
    for r in result_set:
        print(r)
    # Update
    update_statement = Piracy.update().where(Piracy.c.date=="2017-12-30").values(ship_type='BigTanker', piracy_area='Port')     
    connection.execute(update_statement)
    
    # Confirm Update : Read
    reselect_statement = Piracy.select().where(Piracy.c.date=="2017-12-30")    
    update_set = connection.execute(reselect_statement)
    for u in update_set:
        print(u)
    
    # Delete
    delete_statement = Piracy.delete().where(Piracy.c.ship_name == 'BERGE ATLAS')
    connection.execute(delete_statement)
    
    not_found_set = connection.execute(reselect_statement)
    print(not_found_set.rowcount)
    
    