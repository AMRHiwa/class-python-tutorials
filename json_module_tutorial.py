# JSON Module
# author : Hiwa Azizi
# 2022
# in this module we want to learn how can work with json

# first we import json module
import json
from re import X

# we wan to creat a string of dictionary 
x = '{"name" : "Hiwa", "country" : "Iran", "city": "Kermanshah"}'

# transform x to dictionary by loads() method from json module
y = json.loads(x)
print(f"y is :\n{y}\ntype of y:{type(y)}")

# we can tranform dictionary to json object by dumps() method form json
# first we need a dictionary
dict1 = {"name": "Neda", "country": "Iran", "city": "JavanRood"}
# now transform into json object(string object)
json_ob = json.dumps(dict1)
print(f"json_ob is :\n{json_ob}\ntype of json_ob:{type(json_ob)}")


# in json we can tranform any type of data like
# 1.dict
# 2.list
# 3.tuple
# 4.set
# 5.string
# 6.int
# 7.float
# 8.boolean
# 9.None
# for example :
val1 = json.dumps({"name":"Hiwa", "Family":"Azizi"})
print(f"val1 is : {val1}, type of val1 : {type(val1)}")

val2 = json.dumps(["Hiwa", "Neda"])
print(f"val2 is : {val2}, type of val2 : {type(val2)}")