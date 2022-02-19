"""
this file wrote by AMR Hiwa 
for practicing with math module and it's methods
2022

"""



# first of all we have to import math module with import order or from ... import
import math



# math.floor(x) 
# we show the ability of floor function from math with a different values
print("num is 13.25315 ")
print("num1 with floor method : ", math.floor(13.25315))

print("num2 is 25")
print(f"num2 with floor method : {math.floor(25)}")

print("num3 is -12.6")
print("num3 with floor method : {}".format(math.floor(-12.6)))



# math.ceil(x)
# we show it's ability with different values
print("num is 13.25315 ")
print("num1 with ceil method : ", math.ceil(13.25315))

print("num2 is 25")
print(f"num2 with ceil method : {math.ceil(25)}")

print("num3 is -12.6")
print("num3 with ceil method : {}".format(math.ceil(-12.6)))



# math.pi
# we can import complete value of the Pi
print(f"the value of pi in math is {math.pi}")



# math.e
# we can import complete value of neper
print(f"the neper number in math is {math.e}")



# math.inf
# we can use infinity value from math module 
print(f"positive infinit in math module is {math.inf}")
print(f"negative infinit value in math is {-math.inf}")



# math.isinf(x)
# for checking that a variable is inf or not we can use math.isinf(x)
print(f"IS {math.inf} infinit value ? {math.isinf(math.inf)} ")
print(f"IS {math.pi} infinit value ? {math.isinf(math.pi)} ")



# math.nan
# we can use or import NaN (Not a Number) with math
print(f"nan or \"not a number\" in math module is : {math.nan}")



# math.isnan(x)
# for checking that a variable is nan or not we can use math.isnan(x)
print(f"Is {math.nan} is NaN : {math.isnan(math.nan)}")
# print(f"Is 10/0 is NaN : {math.isnan(10/0)}")      Error ZeroDivisionError
print(f"Is 0/10 is NaN : {math.isnan(0/10)}")
print(f"Is {math.e} is NaN : {math.isnan(math.e)}")



# math.fabs(x)
# we can use absolute ability with math.fabs(x) like abs(x) builtin function
print(f"num1 is -13.5 , It with fabs function is {math.fabs(-13.5)}")
print(f"num1 is 26.5 , It with fabs function is {math.fabs(26.5)}")
print(f"num1 is -15 , It with fabs function is {math.fabs(-15)}")



# math.factorial(x)
# we can import factorial ability from math module
print(f"factorial of 8 is {math.factorial(8)}")



# math.exp(x)
# we can calculate neper power of x with math.exp(x)
print(f"e power of 5 is : {math.exp(5)}")



# math.log(y [, x])
# we can call logarithm ability from math
# we can calculate logarithm y in base of x with this method math.log(y, x)
# if we don't give it base it calculate of logarithm with neper as base
print(f"logarithm 2 in base 2 is : {math.log(2, 2)}")
# print(f"logarithm 4 in base 1 is : {math.log(4, 1)}")   Error ZeroDivisionError
print(f"logarithm 9 in base 3 is : {math.log(9, 3)}")
print(f"logarithm 2 in base neper is : {math.log(2)}")
print(f"logarithm e in base neper is : {math.log(math.e)}")



# math.sqrt(x)
# we can use square root with math module by math.sqrt(x)
print(f"the square root of 8 is : {math.sqrt(8)}")
print(f"the square root of 16 is : {math.sqrt(16)}")



# math.pow(x, y)
# we can calculate x power of y with math.pow(x, y)
print(f"3 power of 4 is : {math.pow(3, 4)}")



# math.sin(x)
# math.cos(x)
# math.tan(x)
# we can call trigonometric function like sin , cos , tan with radians argument 
print(f"sin of pi is : {math.sin(math.pi)}")
print(f"cos of pi is : {math.cos(math.pi)}")
print(f"tan of pi is : {math.tan(math.pi)}")



# math.degrees(x)
# we can transform radians to degrees with math.degrees(x)
print(f"pi in radian is : {math.degrees(math.pi)} deg")



# math.radians(x)
# we can transform degrees to radians with math.radians(x)
print(f"180 in deg is : {math.radians(180)} radian ")



# we can call sinh , cosh , tanh with math.sinh(x) 
# math.cosh(x) and math.tanh(x)