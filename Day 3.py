# Day 3

"""
topics covered
1. expressions in python
2. string indexing / slicing
3. string methods 
4. for loop in string
5. if-else condition in string
6. string functions
"""

# expressions in python (combination of operators, operands and variables)
"""
 operators are used to perform operations on operands
 operands are the values on which the operators are applied
 variables are the names given to the operands

1. constant expressions
2. arithematic expressions
3. logical expressions
4. comparison expressions
5. assignment expressions
6. conditional expressions
7. string expressions
8. bitwise expressions
"""
# indexing / slicing
"""str = HELLO
         01234   
       -(12345)
    str [0]= H
    str [1]= E
    str [2]= L
    str [3]= L
    str [4]= O
    str [-1]= O
    str [-2]= L
    str [-3]= L
    str [-4]= E
    str [-5]= H
    str [start : end : step] by default [:::]= {1:1:1}
     forward slicing
    str [1:3]= EL
    str [1:5]= ELLO
    str [1:]= ELLO
    str [:3]= HEL
    str [:]= HELLO
    str [1:3:2]= E
     negative / backward slicing
    str [::-1]= OLLEH
    str [::-2]= OLH
    str [::-3]= OE
    str [::-4]= L
    str [::-5]= O
eg- print (str [1:4:2]) = EL
 
  
text = "NIET GREATER NOIDA" # 18 alphabets, can move as desigred in the right
greet = "HELLO WORLD"
print (text[0:5:2])  
print (text[1:20:2])
print (text[-1:-20:-1]) 
print (text[-20:-1:1])
print (greet[:5], text[:4])
print (text[13:19], greet[6:12])
print (text[13:19:2], greet[6:12:2])
"""


# string methods
"""testing = "i'm DiVyA"

#1. string.lower (all letters lowercase)
print (testing.lower())

#2. string.upper (all letters uppercase)
print (testing.upper())

#3. string.title (capitalizes first letter of each word)
print (testing.title())

#4. string.capitalize (only first letter is uppercase)
print (testing.capitalize())

#5. string.casefold (all letters are lowercase, similar to string.lower)
print (testing.casefold())

#6. string.center (center-align string at specified indexing within specified string)
print (testing.center(20,"*"))

#7. string.count (counts the number of times a character appears in string)
print (testing.count("i"))
print (testing.count("i", 1, 6))
print (testing.count ("z"))
print (testing.encode())

#8. string.startswith (checkes if string starts with specified value)
print (testing.startswith("i"))
print (testing.startswith("i", 1, 6))
print (testing.startswith("z"))

#9. string.endswith (checks if string ends with specified value)
print (testing.endswith("A"))
print (testing.endswith("z"))
print (testing.endswith(" ", 1, 4))

#10. string.expandtabs (replaces tab characters with spaces)
print (testing.expandtabs(4))

#11. string.find (returns index of first occurrence of specified value, returns -1 if value is not found)
print (testing.find("i"))
print (testing.find("i", 1, 6))
print (testing.find("z"))
print (testing.find("divya"))
print (testing.find("i'm"))
print (testing.rfind("i'm", 0, len(testing)))

#12. string.lstrip (removes whitespace from the left)
print (testing.lstrip())

#13. string.rstrip (removes whitespace from the right)
print (testing.rstrip())

#14. string.strip (removes all whitespace)
print (testing.strip())

#15. string.replace (replaces specified phrase with given phrase)
print (testing.replace ("i", "I"))

#16. string.split (splits each word of the string into a list)
print (testing.split())

#17. string.index (returns index of the first occurence of given string in string)
print (testing.index("D"))
print (testing.index("DiVyA"))
print (testing.index("m", 0, len(testing)))

#18. string.isdecimal (returns true is all characers are decimals)
txt = "12345"
print(txt.isdecimal())
print(testing.isdecimal())

#19. string.isdigit (returns true if all characters are digits)
print (testing.isdigit())
print (txt.isdigit())

#20. string.islower (returns true if all characters are lowercase)
print (testing.islower())
print (txt.islower())

#21. string.isupper (returns true if all characters are uppercase)
print (testing.isupper())
print (txt.isupper())

#22. string.isspace (returns true if all characters are whitespace)
print (testing.isspace())

#23. string.is numeric (returns true if all characters are numeric)
print (testing.isnumeric())
print (txt.isnumeric())

#24. string.isidentifier (returns true if character is a valid identifier)
print (testing.isidentifier())
print (txt.isidentifier())

#25. string.isalnumc (returns if string is alphanumeric)
erp = "0241csml189"
print (erp.isalnum())
print (erp.isalpha())

#26. string.replace(old, new, times) (replaces character with given character given number of times)
print (testing.replace("DiVyA", "SiMrAn", 1))

#27. string.swapcase (swaps uppercase and lowercase)
print (testing.swapcase)
"""

# for loop in string
"""
msg = "hello"
for i in msg:
    print(i)
for x in "hello":
    print (x)
print (id(msg))
print (id(x)) # unique memory address (refer identity operator)
print (len(msg))
"""

# if / if-else condition in string
"""
msg = "hello"
if msg == "hello":
    print("hello is equal to hello")
else:
    print("hello is not equal to hello")
if "of" in msg:
    print ("present")
else:
    print ("not present")
"""

"""
# string functions
msg = "hello"

#1. min / max function (precedence- cap letters to small letters)
print (min(msg)) 
print (max(msg))

#2. ''.join() function (joins a list of strings)
print ('%'.join (["2", "abc", "22.5"]))

#3. list(enumerate(string)) (creates list of tupples with index and characters of string)
print (list(enumerate(msg)))

#4. ord() function (returns ASCII code of the character)
print (ord(msg[0]))
print (ord("h"))

#5. chr() function (returns the character represented by ASCII number)
print (chr(104))
"""

# count vowels in a string
"""
sen1 = input("enter a sentence: ")
sen2 = "aeiouAEIOU"
count = 0
for i in sen1:
    if i in sen2:
        count += 1
print (count)  
"""   

# reverse word in a sentence
"""
sen = input("enter a sentence: ")
list = sen.split()

rev = ' '.join(reversed(list)) #method 1
print ("reverse of string is: ", rev)

list = list[::-1] #method 2
rev2 = " ".join(list)
print (rev2)
"""

# check if string is pallindrome
"""
str = input("enter a sentence: ")
rev = str[::-1]
if str == rev:
    print ("sentense is pallindrome")
else:
    print ("sentence is not pallindrome")
    """

# check validity of pancard
"""
name = input ("enter your name:")
pan = input("enter your pancard number: ")
if len(pan) == 10 and name == name.alpha:
    print ("pancard is valid")
else:
    print ("pancard is not valid")
    """
# converting each letter of string from uppercase to lowercase
str = input("enter a string: ")
ans = ""
for i in str:
    if i == i.upper:
        ans += i.lower()
    else:
        ans += i.upper()
print (ans)

# homework problems

#1. Convert a string to uppercase and lowercase
text = "Python Programming"
print(text.upper()) # Output: PYTHON PROGRAMMING
print(text.lower()) # Output: python programming


#2. Find the number of occurrences of a substring
text = "banana"
print(text.count("a")) # Output: 3


#3. Check if a string starts and ends with a specific substring
text = "Hello, Python!"
print(text.startswith("Hello")) # Output: True
print(text.endswith("Python!")) # Output: True


#4. Extracting initials from a full name.
names = "input(enter a name: )"
first_name = names.split
first_name = first_name[:1]
print (first_name)


#5. Convert Uppercase to Lowercase
text = input("Enter a string: ")
result = text.lower()
print("Lowercase String:", result)


#6. Convert Lowercase to Uppercase
text = input("Enter a string: ")
result = text.upper()
print("Uppercase String:", result)


#7. Delete All Consonants from a String
text = input("Enter a string: ")
vowels = "AEIOUaeiou"
result = ""


for char in text:
    if char in vowels:
        result += char


print("String without consonants:", result)


#7. Count Different Types of Characters in String
text = input("Enter a string: ")
vowels = consonants = digits = spaces = others = 0


for char in text:
    if char.isdigit():
        digits += 1
    elif char.isalpha():
        if char.lower() in 'aeiou':
            vowels += 1
        else:
            consonants += 1
    elif char.isspace():
        spaces += 1
    else:
        others += 1


print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
print("Other Characters:", others)


#8 Count Number of Words in a Multi-word String
text = input("Enter a string: ")
words = text.split()
print("Number of words:", len(words))


#9. Sort the Characters of a String
text = input("Enter a string: ")
result = ''.join(sorted(text))
print("Sorted String:", result)


#10. Concatenate Two Strings
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")


result = str1 + str2
print("Concatenated String:", result)


#11. Find the Length of a String
text = input("Enter a string: ")
print("Length of String:", len(text))


#12. Find the Length of a String Without Using String Function
text = input("Enter a string: ")
count = 0


for char in text:
    count += 1


print("Length of String:", count)


#13. Print Initials of Any Name
name = input("Enter your full name: ")
words = name.split()


initials = ""
for word in words:
    initials += word[0].upper()


print("Initials:", initials)


#14. Check Whether a String is Palindrome or Not
text = input("Enter a string: ").lower()
if text == text[::-1]:  # Reverse string and compare
    print("Palindrome")
else:
    print("Not a Palindrome")


#15. Lexicographical (Dictionary) Sorting of Names
n = int(input("Enter number of names: "))
names = []


for i in range(n):
    name = input(f"Enter name {i+1}: ")
    names.append(name)


names.sort()
print("Sorted Names in Lexicographical Order:")
for name in names:
    print(name)


        
