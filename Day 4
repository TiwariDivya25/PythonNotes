# Day 4
"""
 topics covered
 1. list, tuple, set, dictionary (syntax)
 2. if-else condition
"""

# list
"""
it is mutable
repetition allowed
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
fruits = [('apple', 'banana', 'cherry'), 'date', 'elderberry']
"""

# tuple
"""
it is immutable
repetition allowed
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
"""

# set
"""
it is unordered, mutable
repetition not allowed
myset = {"abc", 6, 2.5}
"""

# dictionary
"""
it is unordered, mutable
repetition not allowed
key-value pair
mydict = {"name": "John", "age": 30, "city": "Newyork}
"""
# if-else condition
"""
if condition:         (using conditional statements)
     do something
else:
     do something else

example-
age = 25
if age >= 18:
    print("you are an adult")
else:
    print("you are a minor")
"""
# to check if number is divisible by 5 or not
num = int(input("enter a number"))
if num % 5 == 0:
    print("number is divisible by 5")
else:
    print("number is not divisible by 5")    

# to check if number is even or odd
num = int(input("enter a number"))
if num % 2 == 0:
    print("number is even")
else:
    print("number is odd")

# to check if a person can vote
age = int(input("enter your age: "))
if age > 18:
    print ("you are eligible to vote")
else:
    print("you are not eligible to vote")

# to check greatest of three numbers
a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))

if a > b:    # method 1
    if a > c:
        print(a, "is the greatest number")
    else:
        print(c, "is the greatest number")
if b > c:
    print (b, "is the greatest number")
else:
    print (c, "is the greatest number") 

if a > b and a > c:    # method 2
    print(a, "is the greatest number")   
else:
    print(c, "is the greatest integer")  
if b > c:
    print (b, "is the greatest number")
else:
    print (c, "is the greatest number")   

# to check the stage of life
age = float(input("enter age")) 
if (0 < age and age < 13):
    print("child")
elif (13 <= age and age <= 19):
    print("teenager")
elif (19 < age and age < 60):
    print("adult")
elif (60 <= age and age < 150):
    print("senior citizen")
else:
    print("invalid age")    # to check if a number is positive or negative

# to check if year is leapyear
year = int(input("enter year: "))
if year % 4 == 0:
    print("is leap year")
elif (year % 4 == 0) == False :
    print("is not leap year")    
else:
    print("invalid year")    

# calculator
a = int(input("enter first operand: "))
b = int(input("enter second operand: "))
c = input("enter operator: ")

if c == "+":
    print(a+b)
elif c == "-":
    print(a-b)
elif c == "/":
    print(a/b)
elif c == "*":
    print(a*b)
else:
    print("invalid operator")
    
# quadrant of a point
x = int(input("enter value of x axis: "))
y = int(input("enter value of y axis: "))
if x > 0 and y > 0:
    print("first quadrant")
elif x < 0 and y > 0:
    print("second quadrant")
elif x > 0 and y > 0:
    print("third quadrant")
elif x > 0 and y < 0:
    print("fourth quadrant")
else: 
    print("invalid point")   

# adding two complex numbers
a = complex(input("enter first complex number: "))
b = complex(input("enter second complex number: "))
print (a+b)  

# find roots of a quadratic equation
import math
a = int(input("enter coefficient of x^2: "))
b = int(input("enter coefficient of x: "))
c = int(input("enter constant: "))
d = (b**2) - (4*a*c)
if d > 0:
    print("roots are real and distinct")
    print((-b-math.sqrt(d))/(2*a))
    print((-b+math.sqrt(d))/(2*a))
elif d == 0:
    print("roots are real and equal")
else:
    print("roots are imaginary")

# key value of days of a week
days = {1:"monday", 2:"tuesday", 3:"wednesday", 4:"thursday", 5:"friday", 6:"saturday", 7:"sunday"}
a = int(input("enter number of the day: "))
print(days[a])
b = (input("enter day: "))
if b in days.values():
    print(a)

# colors starting from a word
colors = {"r":("red"), "b":("blue", "brown", "black"), "g":("green", "golden"), "y":("yellow")}
a = input("enter a letter:")
print(colors[a])
if a not in colors:
    print("invalid color")

