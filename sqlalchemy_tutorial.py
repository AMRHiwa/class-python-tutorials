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
result = engine.execute('SELECT * FROM users')

# we can fetch first data by fetchone() or all data by fetchall()
result_one = result.fetchall()
print(type(result_one))
# if we used fetchall() then we can use .items()
# print(type(result_one.items()))
print(result_one)

print(len(result_one))

# we can use pandas to load data with sqlalchemy
# first we need to install pandas by :
#       pip install pandas
