"""
author : Hiwa Azizi
example tutorials for datetime modul in python
15/02/2022
"""




#-------example 1----------
"""
in this example we want to
get today information by 
datetime.now()
"""
import datetime

# get information about time and date of now
now = datetime.datetime.now()       

# show the information 
print(now)                          

# show type of variable now
print(f"type of now variable is : {type(now)}")     





#-------example 2-----------
"""
in this example we want to get
today's information by datetime.today()
"""
import datetime

# get date information of today
today = datetime.datetime.today()

# show the information
print(today)






#-------example 3---------
"""
in this example we want to create
a date object by date()
"""
import datetime

# make a object for storaging date in it
object_of_date = datetime.date(1998,10,13)

# show the info
print(object_of_date)






#--------example 4----------
"""
we want to get today's 
information by date.today()
"""
from datetime import date

# make a variable to storage date of today
today = date.today()

# show the info
print(today)





#--------example 5-----------
"""
in this example we want to work 
with uinx hour by date.fromtimstamp()
"""
from datetime import date

# make a variable to storage a information
timestamp = date.fromtimestamp(2525252525)

# show the info
print(timestamp)






#--------example 6------------
"""
in this example we want to work
day , month and year attribute of 
date object
"""

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
"""
in this example, we want to make a
time object by three ways
"""

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
"""
in this example, we want to work 
with hour, minute and second attributes 
in time object
"""

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
"""
in this example we want to create a 
datetime object with date and time
"""

from datetime import datetime

# datetime(year, month, day)
a = datetime(1998, 2, 18)
print("date of burn of love \na = ", a)

# datetime(year, month, day, hour, minute, second)
b = datetime(1998,2,18,13,30,40)
print("b = ", b)






#--------example 10-----------
"""
in this example we want to work 
with datetime attributes like day
, hour, month and ect"""

from datetime import datetime

# datetime(year, month, day, hour, minute, second, microsecond)
a = datetime(1998, 2, 18, 13, 30, 40)

# show the year
print(f"year : {a.year}")

# show the month
print(f"month : {a.month}")

# show the day
print(f"day : {a.day}")

# show the hour
print(f"hour : {a.hour}")

# show the minute
print(f"minute : {a.minute}")

# show the second
print(f"second : {a.second}")






#---------example 11------------
"""
in this example we want to calculate 
difference between to time and date
"""

from datetime import date

# make 2 variable of date for calculate of difference between of them
# date(year, month, day)
date1 = date(year=1998, month=2, day=18)
date2 = date(1998, 10, 13)

# create a variavle to storage the calculate 2 date
difference_date = date1 - date2

# show the dates and difference
print(f"date 1 : {date1}")
print(f"date 2 : {date2}")
print(f"difference : {difference_date}")

# show type of difference_date
print(f"type of difference date : {type(difference_date)}")






#-----------example 12------------
"""
in this example we want to calculate 
difference between two objects of datetime
"""

from datetime import datetime

# make 2 variable of date for calculate of difference between of them
# datetime(year, month, day, hour, minute, second)
date3 = datetime(year=1998, month=2, day=18, hour=23, minute=15, second=30)
date4 = datetime(1998, 10, 13, 14, 40, 44)

# create a variavle to storage the calculate 2 date
difference_date = date3 - date4

# show the dates and difference
print(f"date 1 : {date3}")
print(f"date 2 : {date4}")
print(f"difference : {difference_date}")

# show type of difference_date
print(f"type of difference date : {type(difference_date)}")






# ----------example 13-------------
"""
in this example we want to create two 
timedelta's objects and calculate 
difference between of them
"""

from datetime import timedelta

# make 2 variable to storage 2 difference date
t1 = timedelta(weeks=5, days=6, hours=12, minutes=45)
t2 = timedelta(days=25, hours=44, minutes=540)

# create another variable to storage result of calculate of difference
t3 = t1 - t2

# show the difference
print(t3)





#--------example 14-------------
"""
in this example we want to create two 
timedelta's objects and calculate 
difference between of them and work 
with negative timedelta
"""


from datetime import timedelta

# create 2 variable to storage 2 date
t1 = timedelta(seconds= 33)
t2 = timedelta(seconds= 54)

# calculate 
t3 = t1 - t2

# show the difference time
print(f"t3 = {t3}")

# show the absolut difference time
print(f"t3 = {abs(t3)}")






#---------example 15------------
from datetime import timedelta

# create a variable to storage a date for calculate to second
t = timedelta(days=5, hours=25, seconds=325)

# show the calculate of t to the second
print(f"total seconds : {t.total_seconds()}")






#--------example 16------------
from datetime import datetime

# current date and time
now = datetime.now()

# transform time to the string with strftime method
t = now.strftime("%H:%M:%S")

# show the result
print(f"time : {t}")

# transform now to the string with month/day/year Hour:Minute:Second (usa calendar)
s = now.strftime("%m/%d/%Y, %H:%M:%S")

# show the result
print(f"date and time : {s}")

# transform now to the string with day/month/year Hour:Minute:Second (uk calendar)
s2 = now.strftime("%d/%m/%Y, %H:%M:%S")

# show the result
print(f"date and time : {s2}")




#--------example 17---------
from datetime import datetime

# create a variable to storage a str date
date_str_Hiwa = "13 October, 1998"
date_str_Neda = "18 February, 1998"

# show the dates
print(f"date of Hiwa : {date_str_Hiwa}")
print(f"date of Neda : {date_str_Neda}")

# create variables to storage object time 
date_object_Hiwa = datetime.strptime(date_str_Hiwa, "%d %B, %Y")
date_object_Neda = datetime.strptime(date_str_Neda, "%d %B, %Y")

# show the dates
print(f"date of Hiwa (datetime object) : {date_object_Hiwa}")
print(f"date of Neda (datetime object) : {date_object_Neda}")





# -----------example 18-----------
from datetime import datetime
import pytz

# create a variable to storage date and time of now
local = datetime.now()

# show the information
# strftime("month/day/year , hour:minute:second" )
print("Local : {}".format(local.strftime("%m/%d/%Y , %H:%M:%S")))

# getting timezone information with pytz modul
tz_NY = pytz.timezone("America/New_York")

# getting time and date of now with american timezone and storage it in a variable
datetime_NY = datetime.now(tz_NY)

# show the time and date with american timezone
print("time and date in New York : {}".format(datetime_NY.strftime("%m/%d/%Y , %H:%M:%S")))

# getting timezone information with pytz modul
tz_London = pytz.timezone("Europe/London")

# getting time and date of now with american timezone and storage it in a variable
datetime_London = datetime.now(tz_London)

# show the time and date with american timezone
print("time and date in London : {}".format(datetime_London.strftime("%m/%d/%Y , %H:%M:%S")))
