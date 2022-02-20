"""
Author : Hiwa Azizi
OS module and it's methods
2022
"""

# we have to import os module in our files like this
from fileinput import filename
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

# show the files with custom name of file (for example we want file
#  that name starts with 'm' or 'd')
for root, directory, file in os.walk(os.getcwd()):
    for f in file:
        if f[0] == "m" or f[0] == "d":
            print(f)

# show files and their address in current address
for root, directory, file in os.walk(os.getcwd()):
    for f in file:
        print(root + "\\" + f)
# if we copy which of them address and paste in Run window, we can run that

# show all directory, root, files in os.walk()
for dirpath, dirname, filename in os.walk(os.getcwd()):
    print(f"current path : {dirpath}")
    print(f"directories : {dirname}")
    print(f"files : {filename}", end="\n\n")


# show the what is the os.walk and what's it type
print(f"what is in os.walk(os.getcwd()): {os.walk(os.getcwd())}")
print("type of os.walk(os.getcwd()) : {}".format(type(os.getcwd())))




# os.mkdir("address and directory name" or "directory name")
# we can make a directory by this method in current directory or custom directory
# os.mkdir("test_folder")




# os.rmdir("address and directory name" or "directory name")
# we can delete a empty directory by this method
# os.rmdir("test_folder")




"""
 for delete not empty directories you can use this way
    first : you have to import shutil module
    second : use shutil.rmtree("name of directory")
your directory with it's files all deleted now
"""
# For example, suppose you have a "new folder" list and it contains a lot of files 
# import shutil
# shutil.rmtree("New folder")




# os.mkdirs("dir_name/first_sub_dir_name/second_sub_of_sub_dir_name/ ...")
# by this method you can create a directory with sub directories
# os.makedirs("A/B/C/D") 




# os.removedirs(""dir_name/first_sub_dir_name/second_sub_of_sub_dir_name/ ..."")
# by this method you can delete a directory with it's subdirectories
# os.removedirs("A")     Error  OSError: [WinError 145] The directory is not empty: 'A'
# os.removedirs("A/B/C/D")




# os.rename("current name", "new name")
# by this method we can rename the file (suppose you have f.txt in current directory)
# os.rename("f.txt", "name.txt")



# os.stat("name and address")
# this method return the stat of one file
# print("stat of file : {}".format(os.stat("math_module_practice.py")))



# os.environ["UserProfile"]
# this attribute show your profile direction
# print(os.environ["UserProfile"])




# os.environ.keys()
# now we can show the attribute of environ
list_keys = os.environ.keys()
for key in list_keys:
    print("{} : {}".format(key,  os.environ.get(key)))





# os.path.exist("name and address")
# Check for the presence or absence of a file
print("is there a time_practice.py file in here : {}".format(os.path.exists("time_practice.py")))
