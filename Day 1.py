import math

"""
topics covered-
1. algorithm and flowchart
2. first program
3. ways of printing
4. basic logic and programs
"""
# algorithm and flowchart

"""eg- sum of 2 numbers
   1. start
   2. enter input a and b
   3. sum = a + b
   4. print sum 
   
   q1- average of 3 numbers
   1. start
   2. enter input a, b and c
   3. sum = a + b + c
   4. avg = sum / 3
   5. print avg
   6. end
   
   q2- swap 2 numbers
     - using third variable
   1. start
   2. enter input a and b
   3. temp = b
   4. b = a
   5. a = temp 
   6. print a, temp
   7. end
     - without using third variable
   1. start
   2. enter input a and b
   3. a = a + b
   4. b = a - b
   5. a = a - b
   6. print a, b
   7. end

   Q3- find area and perimeter of a circle
   1. start
   2. enter input r
   3. area = pi * r * r
   4. perimeter = 2 * pi * r
   5. print area, perimeter
   6. end

   q4- check if number is divisible or not
   1. start
   2. enter input n
   3. if (n % 7 == 0)
   4. print n
   5. end

   q5- checking greatest number
   1. start
   2. enter input a, b, c
   3. if a > b, and a > c
   4. print a is greatest number
   5. else print c is greatest
   6. if b > c print b is greater nuber.
   7. else print c is greatest
   8. end

   q6- check if number is armstrong
   1. start
   2. enter input int
   3. calculate no. of digit d in the number
   4. initialize sum = 0
   5. extract the digit from number
   6. calculate the cube of the digit and add to sum
   7. repeat step 5 and 6 for all the digit in the number
   8. if sum is equal to number then print number is armstrong
   9. else print number is not armstrong
   10. end

   q7- factorial n
   1. start
   2. enter input n
   3. for ( i = 1, i ++, i < 1 )
   4. n = n * i
   5. print n
   6. end

   """

# first program
"""print ( "hello world" )
print ( "I'm excited to learn." )
name = "Divya"
age = 18
print ( "My name is " + name + " and I am " + str(age) + " years old." )
a = 5
print ( a )"""

# print with string formatting ( % s, d, f)
"""name = "Divya"
age = 18
print ( " %s is %d years old " % ( name, age))"""

# print using f strings ( formatted string literals )
"""name = "Divya"
age = 18
print ( f"name: {name}, age: {age}" )
print ( "name: {}, age: {}" .format (name, age) )
print ( f"my name is {name} \nmy age is {age}" )

item = 3
day = "wednesday"
price = 50
print ("i want {0} pieces of {2} by {1}".format ( item, day, price))

print ("apple", "banana", "cherry", sep= ";")
print ("niet", "greater", "noida", sep="-")

print ( "hello", end= ", ")
print ("world")

print ("Simran", "Divya", "Priyanshu", sep=",")"""

#homework problems

# Find the Average of Three Numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

average = (a + b + c) / 3
print("Average:", average)


# Calculate Sum of 5 Subjects and Find Percentage
subjects = []
for i in range(1, 6):
    marks = float(input(f"Enter marks for subject {i}: "))
    subjects.append(marks)

total = sum(subjects)
percentage = (total / 500) * 100

print("Total Marks:", total)
print("Percentage:", percentage)


# Find Gross Salary
basic_salary = float(input("Enter Basic Salary: "))

HRA = 0.2 * basic_salary  # 20% of basic
DA = 0.5 * basic_salary   # 50% of basic
gross_salary = basic_salary + HRA + DA

print("Gross Salary:", gross_salary)


# Calculate Area of Circle
radius = float(input("Enter radius of the circle: "))
area = 3.14159 * radius * radius
print("Area of Circle:", area)


# Calculate Area of Rectangle
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
area = length * breadth
print("Area of Rectangle:", area)


# Calculate Area of Square
side = float(input("Enter side length of square: "))
area = side * side
print("Area of Square:", area)


# Calculate Area and Circumference of Circle
radius = float(input("Enter radius of the circle: "))
area = 3.14159 * radius * radius
circumference = 2 * 3.14159 * radius

print("Area:", area)
print("Circumference:", circumference)


# Calculate Area of Scalene Triangle
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# Semi-perimeter
s = (a + b + c) / 2

# Heron's formula
area = math.sqrt (s * (s - a) * (s - b) * (s - c)) 
print("Area of Scalene Triangle:", area)


# Calculate Area of Right Angle Triangle
base = float(input("Enter base: "))
height = float(input("Enter height: "))

area = 0.5 * base * height
print("Area of Right Angle Triangle:", area)


# Calculate Area of Trapezium
a = float(input("Enter length of first parallel side: "))
b = float(input("Enter length of second parallel side: "))
height = float(input("Enter height: "))

area = 0.5 * (a + b) * height
print("Area of Trapezium:", area)