#Abstract Class -> An abstract method is a method that has a declaration but does not have an implementation.
"""
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def show(self):
        pass
class Circle(Shape):
    def show(self):
        print("It is a Circle")
class Triangle(Shape):
    def show(self):
        print("It is a Triangle")
obj_c = Circle()
obj_c.show()
obj_t = Triangle()
obj_t.show()


from abc import ABC,abstractmethod                      #ABS->Abstract Base Classes
class Sports(ABC):
    def display(self):
        pass
class Cricket(Sports):
    def display(self):
        print("Cricket")
class Football(Sports):
    def display(self):
        super().display()
        print("Football")
obj_c = Cricket()
obj_c.display()
obj_f = Football()
obj_f.display()


#Thread
from time import sleep
from threading import *
class One(Thread):
    def run (self):
        for i in range(5):
            print("Hi")
            sleep(2)
class Two(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)                                #Every Interval of 1 seconds the print statement is Executed
obj_1 = One()
obj_1.start()
obj_2 = Two()
obj_2.start()


#try and exception
a=10
b=2
#b=0
#b="hu"
try:
    c=a//b
    print(c)
    k=int(input("Enter a Number : "))
except ZeroDivisionError as e:
    print("Number Cannot be divided")
except ValueError as v:
    print("Invalid Input")
except TypeError as e:
    print("Invalid Operand")
finally:
    print("Successfully Executed")

#Index out of range
s="fruit"
try:
    # if(type(s)=='int'):
    #     num=s
    # else:
    #     raise ValueError("String Can't be changed into Integer")
    if s[6] in s:
        raise IndexError("String index out of range")
    else:
        print("No Error")
except ValueError as e:
    print(e)
except IndexError as i:
    print(i)
finally:
    print("End")


#GeeksforGeeks -> https://www.geeksforgeeks.org/access-modifiers-in-python-public-private-and-protected/
# program to illustrate protected access modifier in a class

#super class
class Student:

    # protected data members
    _name = None
    _roll = None
    _branch = None

    # constructor
    def __init__(self, name, roll, branch):
        self._name = name
        self._roll = roll
        self._branch = branch

    # protected member function
    def _displayRollAndBranch(self):

        # accessing protected data members
        print("Roll:", self._roll)
        print("Branch:", self._branch)

# derived class
class Geek(Student):

    # constructor
    def __init__(self, name, roll, branch):
        Student.__init__(self, name, roll, branch)

    # public member function
    def displayDetails(self):

              # accessing protected data members of super class
        print("Name:", self._name)

        # accessing protected member functions of super class
        self._displayRollAndBranch()


stu = Student("Alpha", 1234567, "Computer Science")
print(dir(stu))

# protected members and methods can be still accessed
print(stu._name)
stu._displayRollAndBranch()

# Throws error
# print(stu.name)
# stu.displayRollAndBranch()

# creating objects of the derived class
obj = Geek("R2J", 1706256, "Information Technology")
print("")
print(dir(obj))

# calling public member functions of the class
obj.displayDetails()


################## Math Module ####################
import math
n=int(input("Enter a Number : "))
print("The Square root of {} is ".format(n),math.isqrt(n))              #It will eliminate the decimal value of an number
print(dir(math))
print(math.prod([1,2,3],start=2))
print(math.ceil(4.0))                                                   #4
print(math.ceil(4.3))                                                   #5
print(math.floor(2.6))                                                  #2



import re
s="Welcome to Learn Python"
match = re.search(r'Learn',s)
print("Start Index : ",match.start())
print("End Index : ",match.end())
pattern = "W[a-z]*"
result = re.findall(pattern,s)
print(result)

########################## Using Regular Expression ##########################
import re
reg_x = r"^The[A-Z\sa-z]+h$"
l=["The Math","The Earth","Sun"]
for i in l:
    if re.match(reg_x,i):
        print("Matched ",i)
    else:
        print("Unmatched ", i)

s1 = "Hello World!"
pattern1 = r"!$"
match1 = re.search(pattern1,s1)
if match1:
    print("Match Found!")
else:
    print("Match Not Found!")



file = open('sample.txt','r')
for i in file:
    print(i,end=" ") 
file.write(input())
"""

file1 = open('sample.txt','w')                 #It will overwrite content of the existing file
#file1 = open('sample.txt','a')                  #It will append the content of a file
file1.write(input("Enter a text to be inserted : "))
file1.write("\n")
file1.write("Hello\nEveryone")
file1.close()
file = open('sample.txt','r')                   #It will read the Content of a file
for i in file:
    print(i,end="")
file.close()
