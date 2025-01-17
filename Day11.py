# day 11
"""
topics covered-
1. file handling
"""
# file handling

# reading from a file
f = open("demo.txt")
f = open("demo.txt", "r")
print(f.read())

# writing in a file
a = open("demo2.txt", "w")
a.write("Hello, world!")
a = open("demo2.txt")
print(a.read())

print(a.name)
print(a.mode)

f = open("demo.txt")
b = f.read(10)  # reads first 10 characters
print(b)

f = open("demo.txt")
b = f.readline() # reads the first line
print(b)

f = open("demo.txt")
b = f.readline(5) 
print(b)

f = open("demo.txt")
b = f.readlines() # reads all lines, returns list of sentences
print(b)

# append a file
f = open("demo.txt", "a")
f.write("Hello, world!")
f = open("demo.txt")
print(f.read())

f = open("demo.txt")
f = open("writing.txt", "w")
s = "this is python"
f.write(s)

# working with directories
import os
"""# get current directory
current_dir = os.getcwd()
print("your directory:",current_dir)

#change directory
os.chdir("path/to/directory")

#create new directory
os.mkdir("new_folder")
# delete a directory
os.rmdir("new_folder")

#viewing list in a directory
contents = os.listdir()
print(contents)"""

# exception handling
try:
    print(x + 10)
except:
    print("An error occurred")

try:
    print(x + 10)
except NameError:
    print("An error occurred")
except:
    print("Another error occurred")

try:
    print(x + 10)
except ValueError:
    print("An error occurred")
except:
    print("Another error occurred")

try:
    print(x + 10)
except ValueError:
    print("An error occurred")
except:
    print("Another error occurred")
finally:
    print("This will always run")