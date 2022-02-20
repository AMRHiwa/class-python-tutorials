"""
Author : Hiwa Azizi
OS module and it's methods
2022
"""

# we have to import os module in our files like this
import os



# os.getcwd()
# this method used to return current address that you're in now
print("current address right now : ", os.getcwd())



# we save this directory for work in future
current_directory = os.getcwd()



# os.listdir()
# this method use for show all files and folders in current address
print(f"files and folders in current address : {os.listdir()}")
print("type of os.listdir() is {}".format(type(os.listdir())))



# os.chdir("address")
# this method use for change directory
os.chdir("C://")
print("Current directory : ", os.getcwd())
os.chdir(current_directory)



# os.walk("address")
# loop for root, directory and file 
# show the folders and it's owners with root
for root, directory, file in os.walk(os.getcwd()):
    print(root) 

# show the directories and subdirectories 
for root, directory, file in os.walk(os.getcwd()):
    print(directory)

# show the directories and subdirectories without empty directories
for root, directory, file in os.walk(os.getcwd()):
    if len(directory) != 0:
        print(directory)

# show the files in current directory
for root, directory, file in os.walk(os.getcwd()):
    print(file)

# show the files in current directory with custom type of file
for root, directory, file in os.walk(os.getcwd()):
    for f in file:
        if f.endswith(".py"):       # or we can use this order , if ".py" in f : 
            print(f)

# show the files with custom name of file (for example we want file that name starts with 'm' or 'd')
for root, directory, file in os.walk(os.getcwd()):
    for f in file:
        if f[0] == "m" or f[0] == "d":
            print(f)

# show the what is the os.walk and what's it type
print(f"what is in os.walk(os.getcwd()): {os.walk(os.getcwd())}")
print("type of os.walk(os.getcwd()) : {}".format(type(os.getcwd())))




