import sqlalchemy
import sqlalchemy.orm

###creating one-time global object called Engine
###with :memory: we do no need to create a new file
engine = sqlalchemy.create_engine("sqlite+pysqlite:///:memory:", echo=True)

###called the text() construct, which allows us to write SQL statements as textual SQL
#with engine.connect() as conn:
    #result = conn.execute(sqlalchemy.text("SELECT * FROM test_table"))
    #print(result.all())

###commit the changes to DB
with engine.connect() as conn:
    conn.execute(sqlalchemy.text("CREATE TABLE test_table (x int, y int)"))  ###first transactional statement
    conn.execute(
        sqlalchemy.text("INSERT INTO test_table (x, y) VALUES (:x, :y)"),
        [{"x": 1, "y": 1}, {"x": 2, "y": 4}, {"x": 6, "y": 8}, {"x": 9, "y": 10}]
    ) ###second transactional statement
    conn.commit() ###method which commits the transaction

counter = 0

with engine.connect() as conn:
    result = conn.execute(sqlalchemy.text("SELECT x, y FROM test_table"))
    print (result)
    for row in result:
        #print(f"x: {row.x}  y: {row.y}")
        print (f'Column x: {row[0]}')
    #for row in result:
        #y = row.y
    # illustrate use with Python f-strings
        #print(f"Row: {row.x} {y}")

value_to_compare = 4
with engine.connect() as conn:
    result = conn.execute(sqlalchemy.text(f"SELECT x, y FROM test_table WHERE y > {value_to_compare}"))
    ###alternative solution: result = conn.execute(sqlalchemy.text(f"SELECT x, y FROM test_table WHERE y > :y"), {"y":4})
    print (result)
    for row in result:
        #print(f"x: {row.x}  y: {row.y}")
        print (f'Column x: {row[0]}')


###Insert values into table
###A key behavioral difference between “execute” and “executemany” is that the latter doesn’t support returning of result rows, even if the statement includes the RETURNING clause.
with engine.connect() as conn:
    conn.execute(
        sqlalchemy.text("INSERT INTO test_table (x, y) VALUES (:x, :y)"),
        [{"x": 11, "y": 12}, {"x": 13, "y": 14}],
    )
    conn.commit()
    result = conn.execute(sqlalchemy.text("SELECT * FROM test_table"))
    for row in result:
        print(f"x: {row.x}  y: {row.y}")



stmt = sqlalchemy.text("SELECT x, y FROM test_table WHERE y > :y ORDER BY x, y")
with sqlalchemy.orm.Session(engine) as session:
    result = session.execute(stmt, {"y": 6})
    for row in result:
        print(f"from the session x: {row.x}  y: {row.y}")
    session.commit()

###The example above can be compared to the example in the preceding section in Sending Parameters - we directly replace the call to with engine.connect()
#### as conn with with Session(engine) as session, and then make use of the Session.execute() method just like we do with the Connection.execute() method.

###update some values in the table
with sqlalchemy.orm.Session(engine) as session:
    result = session.execute(
        sqlalchemy.text("UPDATE test_table SET y=:y WHERE x=:x"),
        [{"x": 9, "y": 11}, {"x": 13, "y": 15}],
    )
    session.commit()
    result = session.execute(sqlalchemy.text("SELECT * FROM test_table"))
    for row in result:
        print(f"after the update x: {row.x}  y: {row.y}")