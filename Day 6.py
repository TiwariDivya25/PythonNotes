# Day 6
"""
topics covered:
1. more pattern printing
2. creating functions
"""
# slanted star pattern
for i in range(5):
    for j in range(i):
        print("*", end=" ")
    print("*")

# slanted number pattern
for i in range (1,5):
    print (i, end="")
    for j in range (1,i):
        print(j+1, end="") #j
    print("")
for i in range (1,5):
    print (i, end="")
    for j in range (1,i):
        print(i+1, end="") #i
    print("")

# slanted character printing
for i in range(5):
    for j in range(i):
        print(chr(65+j), end=" ")
    print(chr(65+i))
for i in range(5):
    for j in range(i):
        print(chr(65+i), end=" ")
    print(chr(65+j))

# slanted number printing 2
counter = 1
for i in range(5):
    for j in range(1, i):
        print(counter, end="")
        counter = counter + 1
    print ("")

# slanted character printing 2
counter = 65
for i in range (5):
    for j in range (1, i):
        print (chr(counter), end="")
        counter = counter + 1
    print ("")

# reverse slant number printing
n = int(input("enter the number: "))
for i in range (1, n+1):
    for k in range (n, i, -1):
        print(" ", end="")
    for j in range (1, i+1):
        print(j, end="")
    print("")

# reverse slant character printing
a = 65
b = 0
n = int(input("enter the number: "))
for i in range (1, n+1):
    for k in range(n, i, -1):
        print(" ", end = "")
    for j in range (1, i+1):
        print(chr(a+b), end = "")
        b = b + 1
    print("")

# reverse slant star printing
n = int (input ("enetr a number: "))
for i in range (1, n+1):
    for k in range (n, i, -1):
        print (" ", end = "")
    for j in range (1, i+1):
        print ("*", end = "")
    print("")

# triangle
n = int(input("enter the number: "))
for i in range (1, n+1):
    for k in range (n, i, -1):
        print(" ", end = "")
    for j in range (1, i+1):
        print(j, end = "")
    for l in range (1, i):
        print(l, end="")
    print("")

# heart pattern
for j in range (1):
    print("  ", end = "")
for k in range (1):
    print("*", end = "")
for l in range (1):
    print("   ", end = "")
for m in range (1):
    print("*", end = "")
for i in range (2):
    for j in range (1):
        print(" ", end = "")
    for k in range (i):
        print("***", end = "")
    for l in range (1):
        print(" ", end = "")
    for m in range (i):
        print("***", end = "")
    print("")
for i in range (5, 0, -1):
    for k in range (4, i-1, -1):
        print(" ", end = "")
    for j in range (i+1, 1, -1):
        print("*", end = "")
    for l in range (i, 1, -1):
        print("*", end="")
    print("")

# functions:
def arithematic(a, b):
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b
    return add, sub, mul, div

# calling the function
add1, sub1, mul1, div1= arithematic(20, 30)
print("Addition: ", add1)

# creating function of full name
def names(fname, lname):  # formal parameter
    name = fname + lname
    return name
name = names("divya ", "tiwari")  #actual parameter
print(name)

# function of factorial
def factorial(n):
    fac = 1
    for i in range (1, n+1):
        fac = fac * i
    return fac
a = factorial(5)
print(a)

# function of prime number
def prime(n):
    for i in range (2, n):
        if n % i == 0:
            print ("not prime")
            break
        else:
            print ("prime")
            break  
prime(7)

# function of fibbonachi series
def fib(n):

# types of required arguments
# 1. positional/required arguments
# 2. keyword arguments
# 3. default arguments
# 4. variable arguments 

# 1. required arguments
 def required(a, b):
     return a + b
# calling the function
 add1 = required(20, 30)
 print("Addition: ", add1)
# 2. keyword arguments
def keyword(a, b):
    return a + b
# calling the function
add1 = keyword(a=20, b=30)
print("Addition: ", add1)
# 3. default arguments
def default(a, b=10):
    return a + b
# calling the function
add1 = default(20)
print("Addition: ", add1)
# 4. variable arguments
def variable(*args):
    return sum(args)
# calling the function
add1 = variable(10, 20, 30, 40, 50)
