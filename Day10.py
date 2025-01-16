# Day 10
"""
topics covered-
1. sets
2. dictionaries
"""

# set
"""
it is unordered, mutable
repetition not allowed
myset = {"abc", 6, 2.5}
"""
myset = {"abc", 6, 7, 8, 2.5, "abc"}
print(type(myset), len(myset), myset)
# print (myset[0]) is wrong since its unordered

 # iterating in a set
for i in myset:
    print(i)

print (10 not in myset, 10 in myset)

 # operations on a set

s1 = {"abc", 6, 7, 8, 2.5, "abc"}
s2 = {1, 2, 3, 4, 5, "a", "b", "c", "abc"}

print(s1.union(s2), s1 | s2) # includes all elemens from both the sets
print(s1.intersection(s2), s1 & s2) # includes all common elements from both the sets

print(s1.difference(s2), s1 - s2) # includes elements in s1 but not in s2: (s1) - (s1 & s2)
print(s1.symmetric_difference(s2), s1 ^ s2) # excludes elements common in s1 and s2 from s1: (s1 + s2) - (s1 & s2)

s1.intersection_update(s2)
print(s1) # updates s1 with elements common in s1 and s2
s1.difference_update(s2)
print(s1)

 # set methods 
s1 = {"abc", 6, 7, 8, 2.5, "abc"}
s2 = {1, 2, 3, 4, 5, "a", "b", "c", "abc"}

s1.update(s2) # adds the elements of s2 in s1 ignoring repetition 
print (s1)

s1.add(10) # adds element to s1
print(s1)

s2.remove(1) # removes element from s2
print(s2)

s1.discard("f") # discards element from s1 but does not give error if element not in s1
print (s1)

s1.pop() # removes arbitrary element from s1
print (s1)

s1.clear() # removes all elements from s1 set()
print (s1) 

print(s1.isdisjoint(s2)) # returns True for null intersection

print(s1.issubset(s2), s1 <= s2) # returns True if all elements of s1 are subset of s2

print(s1.issuperset(s2), s1 >= s2) # returns True if all elements of s2 are present in s1

c = s1.copy() # returns a copy of s1
print(c) 

s2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
print(any(s2)) # returns True if any element in s1 is true (0, 1)
print(all(s2)) # returns True if all elements in s1 are true (0, 1)
 # ensure that set contains the same datatypes for the following, else type error-
print(max(s2))
print(min(s2))
print(sum(s2))
print(sorted(s2))

for i in enumerate(s2):
    print(i) # returns index and value of each element in s2

# dictionary
"""
it is unordered, mutable
repetition not allowed
key-value pair
mydict = {"name": "John", "age": 30, "city": "Newyork}
"""
# note- empty dictionary = {}, empty set = set()

mydict = {"name": "John", "age": 30, "city": "New york"}
print(mydict)
print(mydict["name"], mydict["age"], mydict["city"])

 # add a new item
mydict["country"] = "USA"
print(mydict["country"])

 # update an existing item
mydict["age"] = 31  
mydict["address"] = "unknown"
print(mydict["age"], mydict["address"])

 # delete an item
del mydict["address"]

 # clear dictionary
mydict.clear()
print(mydict)

"""del mydict
print(mydict) # returns error since mydict is deleted from memory"""

 # copy command
mydict = {"name": "John", "age": 30, "city": "New york"}
mydict2 = mydict.copy()
print(mydict2)

 # length command 
print(len(mydict))

 # get method
print(mydict.get("name"))
print(mydict.get("age"))
print(mydict.get("city"))
 
 # access all keys / values
print(mydict.items()) # list of key value pairs
print(mydict.values()) # list of values
print(mydict.keys()) # list of keys

 # update method
mydict = {"name": "John", "age": 30, "city": "New york"}
d = {"roll no": 17, "name": "divya"}
mydict.update(d)
print(mydict)

# nested dictionary
d1 = {
    "divya":{
        "age": 18,
        "city": "noida"
    },
    "simran":{
        "age": 19,
        "city": "gorakhpur"
    },
    "priyanshu":{
        "age": 20,
        "city": "patna"
    }
}
d2 = {'divya': {'age': 18, 'city': 'noida'}, 'simran': {'age': 19, 'city': 'gorakhpur'}, 'priyanshu': {'age': 20, 'city': 'patna'}}

print(d1)
print(d1 == d2)

divya = {"age": 18, "city": "noida"}
simran = {"age": 19, "city": "gorakhpur"}
students = {"divya": divya, "simran": simran}
print(students)

for key in d1:
    print(key, end = " ")
print()
for value in d1.values():
    print(value, end = " ")
print()

#dict.fromkeys(seq, val)
subjects = ["math", "science", "english"]
marks = dict.fromkeys(subjects, 0)
print(marks)

circumference = {}
"""for i in range (5):
    x = int(input("enter radius: "))
    circumference[x] = 2*3.14*x
print(circumference)"""

cube = {x:x**3 for x in range(5)}
print(cube)

cube = {x:x**3 for x in range(11) if x % 2 == 0}
print(cube)

d1 = {x:x/100 for x in range (11) if x % 3 == 0} # cm to m for x divisible by 3
d2 = {x:x*100 for x in range (11) if x % 3 == 0} # m to cm for x divisible by 3
print (d1, d2)

# store sparce as a dictionary
matrix = [[0, 0, 0, 1, 0], [2, 0, 0, 0, 3], [0, 0, 0, 4, 0]]
dict = {}
for i in range(3):
    for j in range(5):
        if matrix[i][j] != 0:
            dict[(i, j)] = matrix[i][j]
print(dict)

# zip function
a = [1, 2, 3, 4, 5, 6]
b = [2, 3, 4, 5, 6, 7, 8, 9]
dic = dict(zip(a, b))
print (dic)

# regular expressions
import re

text = "this is niet gn"
x = re.findall("^t", text) # matches at the beginning of the line
print (x)
x = re.findall("\Athis", text) 
print (x)

x = re.findall("this$", text) # matches at the end of the string
print (x)
x = re.findall("et$", text) 
print (x)

x = re.findall("t\B", text) 
print (x)

x = re.findall("\D", text) 
print (x)

x = re.findall("\d", text) 
print (x)

x = re.findall("\s", text) # returns number of spaces
print (x)

x = re.findall("^\S", text) 
print (x)

x = re.findall("\w", text) 
print (x)

x = re.findall("\W", text) 
print (x)

x = re.findall("[a-n]", text) 
print (x)

x = re.findall("[]", text) 
print (x)


# homework problems
#1. remove duplicates from a list
l = [1, 1]
s = set(l)
l = list(s)
print(l)

#2. count frequency of each word in a sentence 
sen = input("enter a sentence: ")
count = {}
for i in sen:
    if i not in count:
        count[i] = 1
    else:
        count[i] += 1
print (count)

