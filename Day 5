# day 5

"""
topics covered-
1. while loop
2. for loop 
"""

# while loop
"""
i = 0
while i < 5:
    print(i)
    i += 1
    # output- 0 1 2 3 4
    """
i = 0
while i < 10:
    print("hello")
    i += 1

# for loop
"""
for i in range(5):
    print(i)
    # output- 0 1 2 3 4
    """
for i in range (0,10):
    print("hello")
    i += 1

# checking odd / even numbers from 1 to 50
a = int(input("enter starting limit: "))
b = int(input("enter ending limit: "))
even = 0
odd = 0
for i in range(a,b+1):
    if i % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print ("even:", even)
print ("odd:", odd)

# sum of numbers and their average
a = int(input("input total number of digits you want to average: "))
sum = 0
i = 1
while i <= a:
    print("input number", i, ": ")
    b = int(input(""))
    sum = sum + b
    i += 1
avg = sum / a
print ("average :", avg)

# prime number or not
a = int(input("enter number: "))
b = 0
for i in range (2, a):
    if a % i == 0:
        b = 1
        break
if (b==0):
    print("it is a prime number")
else:
    print("it is not a prime number")

# prime number in a range

# factorial of a number
a = int(input("enter number: "))
fatorial = 1
for i in range (1, a+1):
    factorial = factorial * i
    print("factorial of", a, "is", factorial)

# printing the table of a number
a = int(input("enter a number: "))
for i in range (1, 11):
    print (a,"*",i,"=",a*i)

# checking if a number is a perfect number
a = int(input("enter a number: "))
sum = 0
for i in range (1, a):
    if a % i == 0:
        sum = sum + i
if sum == a:
    print("it is a perfect number")
else:
    print("it is not a perfect number")

# print reverse of a number and check if it is palindrome  
a = int(input("enter a number: "))
temp = a
x = 0
while (a != 0):
    b = a % 10
    x = x * 10 + b
    a = a // 10
print (x)    
if temp == x:
    print("it is a palindrome")

# fibbonachi series
first = 0
second = 1
print (first, end = "")
print (second, end = "")
for i in range (0, 10):
    next = first +second
    print (next, end = "")
    first = second
    second = next

# armstrong number
a = int(input("enter a number: "))
x = str(a)
sum = 0 
while (a != 0):
    b = a % 10
    sum = sum + b**len(x)
    a = a//10
if sum == a:
    print ("Armstrong number")
else:
    print ("not armstrong number")

# nested for loop

# pattern printing 
for i in range (4):
    for j in range (4):
        print ("*", end = "")
    print ("")

# numeric pattern
for i in range (4):
    for j in range (4):
        print (j+1, end = "")
    print ("")

for i in range (4):
    for j in range (4):
        print (i+1, end = "")
    print ("")

# break and continue

# disarium number
n = int(input("enter a number: "))
l = str(n)
sum = 0
temp = n
for i in range (0, len(l)):
    r = int(l[i])
    sum = sum + (r ** (i+1))
if sum == temp:
    print("disarium number")
else:
    print("not a disarium number")

# calculating value of nCr
n = int(input("enter value of n: "))
r = int(input("enter value of r: "))
fac1 = 1
fac2 = 1
fac3 = 1
for i in range (1, n+1):
    fac1 = fac1*i
    i = i+1
for j in range (1, (n-r)+1):
    fac2 = fac2*j
    j = j+1
for k in range (1, r+1):
    fac3 = fac3*k
    k = k+1
print (fac1/(fac2*fac3))

# sum of all prime numbers 1 to 1000
sum = 0
for i in range (2, 1000):
    for j in range (2, i):
        if (i % j == 0):
            break
        else:
            sum = sum + 1
print (sum)

# print sum of the following series 
# (1) + (1+2) + (1+2+3) ...
n = int(input("enter the number of terms you want to add: "))
sum = 0
for i in range (1, n+1):
    sum1 = 0
    for j in range (1, i+1):
        sum1 = sum1 + j
    sum = sum + sum1
print (sum)

# series of sum of factorial
n = int(input("enter the number of terms you want to add: "))
sum = 0
for i in range (1, n+1):
    fac = 1
    for j in range (1, i+1):
        fac = fac*j
    sum = sum + fac
print (sum)

# star pattern
r = int (input("enter rows: "))
c = int(input ("columns: "))
for i in range (r):
    for j in range (c-1):
        print("*", end="")
    print("*")

