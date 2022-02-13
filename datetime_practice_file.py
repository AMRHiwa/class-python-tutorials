
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

#--------example 6------------
from datetime import date

# create a variable to storage a date
today = date.today()

# show the day
print(f"day of today: {today.day}")

# show the month
print(f"month of today: {today.month}")

# show the year
print(f"year of today: {today.year}")

#--------example 7-----------
from datetime import time

# time(hour = 0, minute = 0, second = 0)
a = time()
print("a = ", a)

# time (hour and minute and second)
b = time(11, 34, 56)
print("b = ", b)

# time(hour , minute , second)
c = time(hour= 11, minute= 34, second= 56)
print("c = ", c)

# time(hour, minute, second, microsecond)
d = time(11, 34, 56, 234566)
print("d = ",d)

#----------example 8---------
from datetime import time

# make a variable to storage a time
time1 = time(11, 34, 56)

# show the second
print(f"second : {time1.second}")

# show the minute
print(f"minute : {time1.minute}")

# show the hour 
print(f"hour : {time1.hour}")

#print(dir(time))

#----------example 9----------
from datetime import datetime

# datetime(year, month, day)
a = datetime(1997, 2, 18)
print("date of burn of love \na = ", a)

# datetime(year, month, day, hour, minute, second)
b = datetime(1997,2,18,13,30,40)
print("b = ", b)

#--------example 10-----------