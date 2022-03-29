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
plt.show()

# end of loading and reading items from database by alchemysql
