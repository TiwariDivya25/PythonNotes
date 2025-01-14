#day 2

"""
topics covered-
1. input / output
2. keywords and identifiers
3. data types and variables
4. operators
5. type concersion / typecasting
"""

# input / output
a = int(input("input first number"))
b = int(input("input first number"))
product = a * b
print (product)

a = input ("enter your name")
b = input ("enter your surname")
print ("hello {} {} nice to meet you".format(a, b))
print ("hello {1} {0} nice to meet you".format(b,a))
print ("hello", a, b, "nice to meet you") #will give space in output
print ("hello" + a + b + "nice to meet you") #wont give space in output

# area and perimeter of circle
r = int(input("enter radius of circle"))
area = 3.14 * r * r
perimeter = 2 * 3.14 * r
print = ("area = ", area)
print = ("perimeter = ", perimeter) 

# swapping two numbers
a = int(input("enter first number"))
b = int(input("enter second number"))
temp = a
a = b
b = temp
print ("swapped numbers are as follows -", a, b)

# adding two float numbers
x = float(input("enter first number"))
y = float(input("enter second number"))
sum = x + y
print ("sum = %.2f" %(sum))

# keywords and identifiers (notes)

# Datatypes 

# numeric
x = 10 #numric
y = 3.14 #float
z = 3 + 4j #complex 
# text
name = "alice" #str
# boolean data typ e
flag = True
#sequence data type
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_range = range (5) #range is not a datatype
# mapping datatypes
my_dictionary = {"name": "alice", "age": 25}
# set datatypes
my_set = {1, 2, 3}
my_frozenset = frozenset ([1, 2, 3])
# noone type
nothing = None

print (x)
print (y)
print (z)
print (type(x)) # to identify datatype of x 
print (type(y))
print (type(z))

# type conversion 
a = 2
b = 2.5
sum = a + b
print (type(a))
print (type(b))
print (type(sum))

# typecasting
x = int (2.5)
y = float (3)
sum = x + y
print (type(x))
print (type(y))
print (type(sum))

# types of operators
x = 2
y = 3

#1. arithmatic - +, -, *, /, //, %, **
print (x + y)
print (x - y)
print (x * y)
print (x / y) # quotient
print (x // y) # quotient (whole part)
print (x % y) # remainder
print (x ** y) # power 

#2. assignment - =, +=, -=, *=, /=, %=, //=, **=
x += y
print (x)
x -= y
print (x)
x *= y
print (x)
x **= y
print (x)
x //= y
print (x)
x %= y
print (x)

#3. comparison - ==, !=, >, <, >=, <= 
print (x == y)
print (x != y)
print (x > y)
print (x < y)
print (x >= y)
print (x <= y)

#4. logical - and, or, not
print ( x < y and x == y )
print ( x < y or x > y )
print ( not (x < y or x > y))

#5. bitwise operator
print ( x & y ) #and
print ( x | y ) #or
print ( x ^ y ) #xor
print ( ~x ) # not (one's complement, two's complement)
print ( x << y ) # left shift
print ( x >> y ) # right shift

#6. membership operator
list = {1, "a", 2.5, 4, 5, 6, .7}
print ("B" in list)
print ("A" in list)
print ("B" not in list)
print ("A" not in list)

#7. identity operator (when memory location of objects are same)
l1 = {1, 2, 3, 4, 5}
l2 = {1, 2, 3, 4, 5}
l3 = l1
print (l1 is not l3) #same object
print (l1 is l3) #true
print (l1 is l2) #false
print (l1 is not l2)
print (l1 == l2)
print (l1 != l2)

# operator precedance - (), **, //, * /, + - (associativity exists left-right, right-left)

# Homework problems

# Find the Area of a Rhombus
diagonal1 = float(input("Enter first diagonal: "))
diagonal2 = float(input("Enter second diagonal: "))

area = (diagonal1 * diagonal2) / 2
print("Area of Rhombus:", area)

#Find the Area of a Parallelogram
base = float(input("Enter base: "))
height = float(input("Enter height: "))

area = base * height
print("Area of Parallelogram:", area)


# Volume and Surface Area of a Cube
side = float(input("Enter side length: "))

volume = side ** 3
surface_area = 6 * (side ** 2)

print("Volume:", volume)
print("Surface Area:", surface_area)


# Volume and Surface Area of a Cuboid
length = float(input("Enter length: "))
width = float(input("Enter width: "))
height = float(input("Enter height: "))

volume = length * width * height
surface_area = 2 * (length * width + width * height + height * length)

print("Volume:", volume)
print("Surface Area:", surface_area)


# Volume and Surface Area of a Cylinder
radius = float(input("Enter radius: "))
height = float(input("Enter height: "))

volume = 3.14159 * radius ** 2 * height
surface_area = 2 * 3.14159 * radius * (radius + height)

print("Volume:", volume)
print("Surface Area:", surface_area)


# Surface Area and Volume of a Cone
radius = float(input("Enter radius: "))
height = float(input("Enter height: "))

slant_height = (radius**2 + height**2)**0.5
volume = (1/3) * 3.14159 * radius**2 * height
surface_area = 3.14159 * radius * (radius + slant_height)

print("Volume:", volume)
print("Surface Area:", surface_area)


# Volume and Surface Area of a Sphere
radius = float(input("Enter radius: "))

volume = (4/3) * 3.14159 * radius**3
surface_area = 4 * 3.14159 * radius**2

print("Volume:", volume)
print("Surface Area:", surface_area)


# Perimeter of Circle, Rectangle, and Triangle
 # Circle
radius = float(input("Enter radius of circle: "))
circle_perimeter = 2 * 3.14159 * radius
print("Perimeter of Circle:", circle_perimeter)

 # Rectangle
length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))
rectangle_perimeter = 2 * (length + breadth)
print("Perimeter of Rectangle:", rectangle_perimeter)

 # Triangle
a = float(input("Enter first side of triangle: "))
b = float(input("Enter second side of triangle: "))
c = float(input("Enter third side of triangle: "))
triangle_perimeter = a + b + c
print("Perimeter of Triangle:", triangle_perimeter)


# Compute Simple Interest
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time in years: "))

simple_interest = (principal * rate * time) / 100
print("Simple Interest:", simple_interest)


# Convert Fahrenheit to Celsius
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

celsius = (fahrenheit - 32) * 5 / 9
print("Temperature in Celsius:", celsius)


# Swap Values of Two Variables (Using Third Variable)
a = int(input("Enter first value: "))
b = int(input("Enter second value: "))

temp = a
a = b
b = temp

print("After Swapping: a =", a, ", b =", b)


# Swap Values of Two Variables (Without Using Third Variable)
a = int(input("Enter first value: "))
b = int(input("Enter second value: "))

a, b = b, a  # Swapping without a third variable

print("After Swapping: a =", a, ", b =", b)

