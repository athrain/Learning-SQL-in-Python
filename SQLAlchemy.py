import sqlalchemy
import pandas as pd

###connect to a database. include echo=True to see what SQL is doing behind the scene
engine = sqlalchemy.create_engine('sqlite:///kaggle_testset.db', echo=True)

dataframe = pd.read_sql_table("Movies", con=engine.connect())

#with engine.connect() as conn:
    #result = conn.execute(sqlalchemy.text("SELECT * FROM Movies"))
    #for row in result:
        #print (row)

print(dataframe.tail())