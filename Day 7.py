# day 7
"""
topics covered
1. more on functions
2. filter
3. map
4. reduce
"""
# function of sum of marks
def sum(*n):
    result = 0
    for i in n:
        result += i
    return result
print (sum(10, 20, 30, 40))

# function of average of marks
def average(*n):
    result = 0
    len = 0
    for i in n:
        result += i
        len += 1
    avg = result/len
    return avg
print (average(10, 20, 30, 40))

# function of calculator
def calculator():
    result = float(input("Enter the first number: "))
    
    while True:
        operator = input("Enter operator (+, -, *, /, = to stop): ")
        
        if operator == "=":  # Stop the calculation
            break
        
        if operator not in ["+", "-", "*", "/"]:
            print("Invalid operator. Please try again.")
            continue
        
        try:
            n = float(input("Enter the next number: "))
        except ValueError:
            print("Invalid number. Please try again.")
            continue
        
        if operator == "+":
            result += n
        elif operator == "-":
            result -= n
        elif operator == "*":
            result *= n
        elif operator == "/":
            if n == 0:
                print("Division by zero is not allowed. Try again.")
                continue
            result /= n
    
    return result

# Run the calculator
result = calculator()
print(f"Final result: {result}")

# local / global variables
x = 10
def function():
    global x
    x = 20
    print(x) # prints 10

# nested functions
def outer():
    outer_var = 10
    def inner():
        global inner_var
        inner_var = 20
        print(outer_var) # prints 10
        print(inner_var) # prints 20
    inner()
    print(outer_var) # prints 10
    print(inner_var) # prints 20
outer()
   
# anonymous / lambda function
square = lambda x: x**2
print(square(5)) # prints 25
sum = lambda x, y: x + y
print(sum(5, 10)) # prints 15

 # multiplication of 3 numbers using lambda fxn
a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))
mul = lambda a, b, c: a * b * c

# example
def my_fxn(n):
    return lambda a : a + n
z = int(input("enter the number: "))
mydouble = my_fxn(z)
print (mydouble(11))

# program o find smaller of teo numbers using lambda function
def small(a,b):
    if a < b :
        return a
    else:
        return b
sum = lambda x, y : x + y
diff = lambda x, y : x - y
print(small(sum(10,20), diff(30, 50))) 

# smallest of 3 numbers using lambda fxn
def small(a,b,c):
    if a < b :
        if a < c:
            return a
        else:
            return c
    elif b < c:
        return b
    else:
        return c
sum = lambda x, y, : x + y
diff = lambda x, y : x - y
mul = lambda x, y : x * y
print(small(sum(10,20), diff(30, 50), mul(5, 10)))

# printing lambda function in a single line
print((lambda x,y : x**y)(2,3))

# example
def func(f,n):
    print(f(n))
    # no need to return due to usage of lambda funtion
twice = lambda x : x * 2
thrice = lambda x : x * 3
func(thrice, 5)
func(twice, 4)

add = lambda x, y: x + y
mul_and_add = lambda x,y,z: x*(y,z)
print (mul_and_add(2,3,4))

# filter map reduce

# filter (requires function and sequence)
# filter even numbers form a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def is_even(n):
    if n % 2 == 0:
        return True  
even= filter(is_even, numbers)
print(list(even))

even = filter(lambda n : n % 2 == 0, numbers)
print(list(even))

# filter prime numbers from a list
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def prime(n):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                break
        else:
            return True
p = filter(prime, numbers)
print(list(p))

# checking eligibility to vote   
people = {} 
for i in range(3):
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    people[name] = age

eligible_members = filter(lambda person: person[1] >= 18, people.items())
eligible_names = [name for name, age in eligible_members]

print("Eligible members are:", eligible_names)


# map (function, sequence)
num = [10, 20, 25, 2, 4, 8, 7]
cube = list(map(lambda x:x**3), num)
print (cube)

# reduce (calls back itself)
from functools import reduce 
list = [20, 12, 52, 22, 19, 7]
large = reduce(lambda x,y: x if x > y else y, list)
print(large)

greatest = reduce(lambda x, y: x if x > y else y)
print(greatest)

# recursion 
# for factorial
def factorial(n):
    if n == 0:
        return 1  # base criteria 
    else:
        return n * factorial(n-1)
print(factorial(5))

# for fibbonachi series
def fib(n):
    if n < 2:
        return n 
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print(fib(10))


