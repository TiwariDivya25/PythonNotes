#OOPS

"""
class Student:
    college_name = "NIET College"
    name = "anonymous" #class attribute

    def __init__(self): #default constructor 
        pass
    
    #parameterized constructor 
    def __init__(self, name, marks): #constructor class always executed
        self.name = name #obj attr > class attr (precedence)
        self.marks = marks

    #methods are functions that belong to objects
    def welcome(self):
        print("welcome student,", self.name)
    
    def get_marks(self):
        return self.msrks


#instance attributes - name, marks
#class attributes - institute name
s1 = Student("Divya", 80)
print (s1.name, s1.marks, Student.college_name)

s2 = Student("Simran", 90)
print (s2.name, s2.marks, Student.college_name)
s2.welcome()
print(s2.get_marks()) 
"""

"""
class Microwave:
    def __init__(self, brand: str, pow_rating: str):
        self.brand = brand
        self.pow_rating = pow_rating

smeg: Microwave = Microwave(brand: "smeg", pow_rating: "B")
print(smeg) 
"""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg score is:", sum/3)

s1 = Student("Divya Tiwari", [99, 98, 97])
s1.name = "Simran Gupta" #can modify attributes of s1 after creating an object s1
s1.get_avg()

# static methods - dont use the self parameter, work at class level rather than object level

class Hello:
    @staticmethod #decorator
    def hi():
        print("Hello")

# abstraction - Hiding the implementation details of a class and only showing the essential features to the user
class Car:
    def __init__(self, type):
        self.type = type

        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("car started...")

car1 = Car("random")
car1.start()

# encapsulation - Wrapping data and functions into a single unit(object)

# bank account

class Account:
    def __init__(self, bal, acc, word):
        self.balance = bal
        self.account_no = acc
        self.__password = word  # private attribute

    #debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("total balance =", self.get_balance())

    #credit method
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("total balance =", self.get_balance())

    #balance method
    def get_balance(self):
        return self.balance 

    #reset password
    def reset_pass(self):
        print(self.__password)

acc1 = Account(10000, 12345, "abcde")
acc1.debit(1000)
acc1.credit(500)

# del keyword - delete object properties or the object itself

del car1.acc # delete attribute
del car1 # delete object

# private attributes and methods - acc.__password

acc1.reset_pass() # can access private attribute using another function in the class

# inheritence - deriving properties or methods from parent class

class ToyotaCar(Car):
    def __init__(self, brand, type):
        super().__init__(type) # super method - access methods of the parent class
        self.brand = brand

car1 = ToyotaCar("prius", "electric")
car2 = ToyotaCar("Toyota", "petrol")

print(car1.brand)
print(car1.start())
print(car1.type)

# types of inheritence - single-level, multi-level,  multiple (multiple parents)

class Fortuner(ToyotaCar): 
    def __init__(self, type):
        self.type = type

car3 = Fortuner("diesel")
car3.start()

# multiple inheritance

class A:
    varA = "welcome to class A."

class B:
    varB = "welcome to class B."

class C(A, B):
    varC = "welcome to class C."

c1 = C()
print(c1.varA, c1.varB, c1.varC)

# class methods - bound to the class and recieves the class as an implicit first argument.
# note - static method can't access or modify class state and generally for utility

class Person:
    name = "anonymous"

    def changeName(self, name):
        # Person.name = name
        # # or self.__class__.name = name

        @classmethod
        def changeName(cls, name):
            cls.name = name

p1 = Person()
p1.changeName("Rahul Kumar")
print(p1.name)
print(Person.name)

# property decorator

class Exam:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        # self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

stu1 = Exam(90, 91, 92)
print(stu1.percentage)

stu1.phy = 80
print(stu1.phy)
print(stu1.percentage)

# Polymorphism - using in many forms
# eg - operator overloading 

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img, "j")

    def __add__(self, num2):  # addition using dunder functions
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg) 

    def __sub__(self, num2):  # substraction using dunder functions
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg) 

num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(4, 6)
num2.showNumber()

# num3 = num1.add(num2) - without dunder add function
# num3.showNumber()

num3 = num1 + num2
num3.showNumber()

# practice questions

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

cir1 = Circle(20)
print(cir1.area())
print(cir1.perimeter())

class Employee:
    def __init__(self, role, dep, sal):
        self.role = role
        self.department = dep
        self.salary = sal

    def showDetails(self):
        print("role =", self.role)
        print("department =", self.department)
        print("salary =", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "75,000")

e1 = Engineer("Elon Musk", 40)
e1.showDetails()

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, odr2):
        return self.price > odr2.price

odr1 = Order("chips", 20)
odr2 = Order("tea", 15)

print(odr1 > odr2) #True