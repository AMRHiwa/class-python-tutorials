"""
this file wrote by AMR Hiwa 
for practicing with math module and it's methods
2022

"""



# first of all we have to import math module with import order or from ... import
import math 

# floor method 
# we show the ability of floor function from math with a different values
print("num is 13.25315 ")
print("num1 with floor method : ", math.floor(13.25315))

print("num2 is 25")
print(f"num2 with floor method : {math.floor(25)}")

print("num3 is -12.6")
print("num3 with floor method : {}".format(math.floor(-12.6)))


# ceil method
# we show it's ability with different values
print("num is 13.25315 ")
print("num1 with ceil method : ", math.ceil(13.25315))

print("num2 is 25")
print(f"num2 with ceil method : {math.ceil(25)}")

print("num3 is -12.6")
print("num3 with ceil method : {}".format(math.ceil(-12.6)))


# we can import complete value of the Pi
print(f"the value of pi in math is {math.pi}")


# we can import complete value of neper
print(f"the neper number in math is {math.e}")


# we can use infinity value from math module 
print(f"positive infinit in math module is {math.inf}")
print(f"negative infinit value in math is {-math.inf}")


# for checking that a variable is inf or not we can use math.isinf(x)
print(f"IS {math.inf} infinit value ? {math.isinf(math.inf)} ")
print(f"IS {math.pi} infinit value ? {math.isinf(math.pi)} ")


# we can use or import NaN (Not a Number) with math
print(f"nan or \"not a number\" in math module is : {math.nan}")


# for checking that a variable is nan or not we can use math.isnan(x)
print(f"Is {math.nan} is NaN : {math.isnan(math.nan)}")
# print(f"Is 10/0 is NaN : {math.isnan(10/0)}")      Error ZeroDivisionError
print(f"Is 0/10 is NaN : {math.isnan(0/10)}")
print(f"Is {math.e} is NaN : {math.isnan(math.e)}")


# we can use absolute ability with math.fabs(x) like abs(x) builtin function
print(f"num1 is -13.5 , It with fabs function is {math.fabs(-13.5)}")
print(f"num1 is 26.5 , It with fabs function is {math.fabs(26.5)}")
print(f"num1 is -15 , It with fabs function is {math.fabs(-15)}")


# we can import factorial ability from math module
print(f"factorial of 8 is {math.factorial(8)}")


# we can calculate neper power of x with math.exp(x)
print(f"e power of 5 is : {math.exp(5)}")