

"""
#-------example 1----------
from dataclasses import dataclass
import datetime

# get information about time and date of now
now = datetime.datetime.now()       

# show the information 
print(now)                          

# show type of variable now
print(f"type of now variable is : {type(now)}")     

#-------example 2-----------
import datetime

# get date information of today
today = datetime.datetime.today()

# show the information
print(today)

#-------example 3---------
import datetime

# make a object for storaging date in it
object_of_date = datetime.date(1998,10,13)

# show the info
print(object_of_date)

#--------example 4----------
from datetime import date

# make a variable to storage date of today
today = date.today()

# show the info
print(today)

#--------example 5-----------
from datetime import date

# make a variable to storage a information
timestamp = date.fromtimestamp(2525252525)

# show the info
print(timestamp)
"""
#--------example 6------------
