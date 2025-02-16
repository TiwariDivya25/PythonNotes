import random
import string

pass_str = string.ascii_letters + string.digits + string.punctuation
len = int(input("Enter the length of your password: "))

password = ""
for i in range (len):
    password += random.choice(pass_str)
print("Your suggested password is: ", password)

# using list comprehension
res = "".join(random.choice(pass_str) for i in range(len))
print("Password using list comprehension: ", res)