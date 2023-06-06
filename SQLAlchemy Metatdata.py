import sqlalchemy

metadata = sqlalchemy.MetaData()

###create primary table with primary Key
user_table = sqlalchemy.Table(
    "user_account",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(30)),
    sqlalchemy.Column("fullname", sqlalchemy.String),
)

print(user_table.c.keys())

###create additional table with foreign key
address_table = sqlalchemy.Table(
    "address",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.ForeignKey("user_account.id"), nullable=False), ###nullable false means the table will not accept NON values for that column
    sqlalchemy.Column("email_address", sqlalchemy.String, nullable=False),
)