# ORM means Object Relation Mapping
# for working with sqlalchemy you have to install 'sqlalchemy' python pakcage
# by this command :
#       pip install sqlalchemy
# also you need to install sql-connector:
#       pip install mysql-connector


# now we import sqlalchemy
# from sqlalchemy import select, insert, create_engine
import sqlalchemy as db

# for create a database in sqlalchemy we can use this method:
#       sqlalchemy.create_engine('dialect+driver://user:pass@host:port/db')
engine = db.create_engine('mysql+mysqlconnector://root:@localhost:3306/pydb')

# making a connection object from sqlalchemy by alchemy.connect()
# connection = db.connect()

# getting values from databases by under order
# 'SELECT * FROM tablename' means select all item from tablename
result = engine.execute('SELECT * FROM users')

# we can fetch first data by fetchone() or all data by fetchall()
result_one = result.fetchall()
print(type(result_one))
# if we used fetchall() then we can use .items()
# print(type(result_one.items()))
print(result_one)

print(len(result_one))

print("____________________________________________")

# we can use pandas to load data with sqlalchemy
# first we need to install pandas by :
#       pip install pandas
# then we need to import it
import pandas as pd
query = "SELECT * FROM users"
data = pd.read_sql_query(query,engine)

print(type(data))
print(data)

print("___________________columns_________________________")
# we can show the database columns by .columns
print(data.columns)

print("____________________dtypes________________________")
# also we can show database types of any columns by .dtypes
print(data.dtypes)

print("____________________head()________________________")
# we can show the head of database's data
print(data.head())


print("___________________max()_________________________")
# we can show max of one or many columns in database like:
print(data[['password', 'username']].max())

print("____________________min()________________________")
# we can show min of one or many columns in database like:
print(data[['password', 'username']].min())

print("_____________________sum()_______________________")
# we can show sum of one or many columns in database like:
print(data[['password', 'username']].sum())

print("______________________describe()______________________")
# we can describe database loads by .describe() method
print(data[["password", "username"]].describe())

print("______________________dropna()______________________")
print(data[["password", "username"]].dropna())

print("______________________paint chart by matplotlib______________________")
import matplotlib.pyplot as plt
import numpy as np

colors = np.random.rand(3)
print(colors)
x = data['password']
y = data['username']

plt.scatter(x, y, c=colors)
plt.title("Data: Username and Password")
plt.xlabel("password")
plt.ylabel("username")
plt.legend(('password', 'username'))
# plt.show()
# end of loading and reading items from database by sqlalchemy


# Querying with sqlalchemy
# Connecting database
# for connecting database we need a 'connector' and 'Connection String'
# for installing connector for each of sql database we need to install :
#       for sqlite, we have to install 'pysqlite'
#       for Postgresql, we have to install 'psycopg2'
#       for mysql,  we must to install 'mysql-connector'
#       for oracle, we must to install 'cx_oracle'
#       for microsoft sqlserver, we must to install 'pyodbc'


# Anatomy of a Connection String
# engine = create_engine('dialect[+driver]://user:password@host:port/dbname[?key= value]')
#       dialect means wich sql that you used like 'mysql'.
#       driver means that option you use to connect like 'mysqlconnector'.
#       user means that username you enter to database by that like 'root'.
#       password means that password you entered in database.
#       host means address host like "localhost".
#       dbname means database name you want it.
#   engine = create_engine('sqlite:///sqlalchemy_sqlite.db')

# create a engine for sqlite:
#   example ->      engine_sqlite = create_engin('sqlite://importing_sqlite.db')

# create a engine for mysql:
#   example ->      engine_mysql = create_engine('mysql+mysqlconnector://root:mysql@localhost:3306/importing_mysql')

# create a engine for postgresql:
#   example ->      engine_postgresql = create_engine('postgresql://hiwa:postgre@localhost:5432/importing_postgres')

# we can show the tables in database:
#     for sqlite you can use this order:
#             engine_sqlite.tabel_names()
#     for mysql you can use this order:
#             engine_mysql.tabel_names()
#     for postgres you can use this order:
#             engine_postgresql.tabel_names()


print("---------------connect to database---------------")
from sqlalchemy import create_engine

engine_mysql = create_engine('mysql+mysqlconnector://root:@localhost:3306/pydb')
print(engine_mysql.table_names())
# end of connecting to database



# Classical Mapping
print("------------Clasical Mapping-----------")
from sqlalchemy import Table, MetaData, Column, Integer, String
from sqlalchemy.orm import mapper

metadata = MetaData()
# create a table
user = Table('users', metadata,
            Column('id', Integer, primary_key=True),
            Column('password', String),
            Column('username',String(150)))

# we need to define a class for 'family_name'
class Users:
    def __init__(self, password, username):
        self.password = password
        self.username = username

# now we need to create a mapper by mapper(ClassName, variable_name of table)
user_mapper = mapper(Users, user)

# create a query
larger = user.select(user.password > 10)
type(larger)

# execute query and show larger
engine.execute(larger).fetchall()

