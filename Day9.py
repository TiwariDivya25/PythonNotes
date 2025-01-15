# day 9
"""
topics covered-
1. making a package in google collab 
2. making a package in jupyter notebook
3. sequence : string, list, tuple
4. packing / unpacking
5. methods
6. tower of hanoi
"""
# making a package in google collab
"""
1. create a new file
2. to create a new package- !mkdir my_package
3. to create a module inside the package- %%writefile my_package/my_module.py
4. create functions inside my_module and override it
5. create a module __init__.py in every package- %%writefile my_package2/__init__.py
6. import your package
7. import desired modules"""

# making a package in jupyter notebook
"""
1. create a file containing functions
2. download file with .py extention
3. open file
4. upload --> select the file you just downloaded and upload it
5. open a new jupyter python file
"""

# packing
# packing is used to store multiple values in a single variable
pack = 1, 2, 3
print(pack)

# unpacking
# unpacking is used to unpack the values from a single variable
a, b, c = 1, 2, 3
print(a, b, c)

# mutable vs immutable sequences
"""
mutable sequences are lists and dictionaries that can be changed after creation
immutable sequences are strings and tuples that cannot be changed after creation
sets are mutable but each element in a set must be immutable 
"""

# methods

# refer day 3 for string methods / functions

# list
"""
it is mutable
it is ordered
repetition is allowed
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
fruits = [('apple', 'banana', 'cherry'), 'date', 'elderberry']
"""

list = [1, "abc", 4.5]
print(list[0])  # prints 1
print(list[1])  # prints abc
print(list[2])  # prints 4.5
print(type(list))
print(type(list[1]))

 # iterating in a list

for i in list:
    print(i)

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in num:
    if i % 3 == 0:
        print(i)

even = []
odd = []
for i in num:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)

num1 = num[2:7:2]
num2 = num[::-1]
print (num1, num2)

print(2 not in num)
print(2 in num)

list[0] = "one"
print(list)

num[::2] = ["two", "four", "six", "eight", "ten"]
print(num)

num[:6:2] = list
print (num)

 # insert command
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
num.insert(9, 10)  #(index, what to insert)
print(num)
num.insert(5, "five")
print(num)
  
 # append command
num.append("ten")  #(inserts rightmost)
print(num)

 # extend command
num.extend(list) # (num = num + list)
print(num)
print(list)
 
 # remove command (removes first occurrence of value
num.remove("ten")
print(num)
print(num)

 # pop command (removes specified index, removes last item in list by default)
num.pop(2)
print(num)

 # delete command (removes specified index, deletes list by default)
del num[10]
print(num)

 # clear commant (empties the list)
num.clear()
print(num)

 # extend command
tup = (1, 2, 3, 4, 5)
num.extend(tup)  # correct
print(num)
"""tup.extend(list) # incorrect since tuple is immutable 
print(tup)"""

# list comprehension
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = [x for x in num]
print(num)

"""cube = []
for i in range(11):
    if i % 2 == 0:
        cube.append(i**3)
print(cube)"""

print ([x**3 for x in num if x % 2 == 0])

"""x = []
for i in num:
    if i % 2 == 0:
        x.append(i)
print (x)"""

print ([x for x in num if x % 2 == 0])

fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
"""f = []
for i in fruits:
    if "a" in i:
        f.append(i)
print(f)"""

print ([x for x in fruits if "a" in x])

 # sorting command
num = [5, 2, 8, 1, 9]
num.sort()  # assending order
print(num)
num.sort(reverse=True)  # decending order
print(num)

  # copy command
n = num.copy()
print(n)
n = num
print(n)

# tuple
"""
it is immutable
it is ordered
repetition allowed
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
"""
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
z = numbers[2:7:2]
print(z)

numbers = list(numbers)
numbers.append(10)
numbers.remove(1)
numbers = tuple(numbers)
print(numbers)

# tower of hanoi

# homework problems

#1. count frequency of each word in a sentence 
sen = input("enter a sentence: ")
for i in sen:
    if i not in sen[:sen.index(i)]:
        print(i, sen.count(i))

#2. filter out vowels from a string
s = input("enter string: ")
vowels = "aeiouAEIOU"
print([x for x in s if x in vowels])

#3. prime numbers 1-50
print ([x for x in range (2, 51) for j in range (2, x) if x % j == 0 == False])