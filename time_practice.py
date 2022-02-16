"""
author : Hiwa Azizi
time modul in python and it's methods
2022
"""
# --------example 1----------
import time

# create a variable to storage the value of seconds past of epoch
seconds = time.time()

# show the result
print(f"seconds since epoch : {seconds}")





# --------example 2---------
import time

# create a variable to storage the value of seconds past of epoch
seconds = time.time()

# create a variable to storage the calculate of local time with epoch time
local_time = time.ctime(seconds)

# show the result
print(f"seconds since epoch : {local_time}")





# -------example 3----------
import time

print("this is a printed immediately")

# Create an interrupt with time.sleep
time.sleep(2)

print("this is a printed after 2 seconds")





