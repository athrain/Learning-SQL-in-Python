###The script allows to connect to database,
### create a table
### and add some values from Pandas dataframe,
### convert PostgreSQL table into Pandas DF

###BEFORE USING - include username, password, DB name + path to additional files/tables

import sqlalchemy
#import psycopg2
import pandas as pd

###connect to PostgreSQL table
engine = sqlalchemy.create_engine('postgresql+psycopg2://USER_NAME:PASSWORD@localhost/DATABASE_NAME')
table_prepared = pd.read_csv(r"FILE_PATH")
print (f'A connection to PostgreSQL was successfully established')

###creates a table in PostgreSQL database
metadata = sqlalchemy.MetaData()

table_name = "test_table"

table = sqlalchemy.Table(
    table_name,
    metadata,
    sqlalchemy.Column("Number", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("Years_of_experience", sqlalchemy.Float),
    sqlalchemy.Column("Salary", sqlalchemy.Integer)
)
metadata.create_all(engine)
print (f'A table {table_name} was succesfully created')

###adding values into database
counter = 0

for row in range (len(table_prepared)):
    salary = table_prepared.iloc[counter,1]
    years_of_experience = table_prepared.iloc[counter,0]
    index_to_be_passed = counter
    with engine.connect() as conn:
        conn.execute(sqlalchemy.insert(table).
                     values
                     (Salary=salary,
                     Years_of_experience=years_of_experience)
                    )
        conn.commit()
    if counter % 10 == 0:
        print (f'Added {counter} rows')
    else:
        pass
    counter +=1

print (f'Values were added to the table. Values added: {len(table_prepared}')

###load PostgreSQL table into Pandas DF

postgres_table = pd.read_sql("test_table", con=engine.connect())
print (f'A table was sucessfully loaded from PostgreSQL to Pandas DF')
