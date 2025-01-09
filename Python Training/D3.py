"""
x=10
def change():
    global x
    x=20
def change1():
    global x
    return x
change()
print(x)
change1()
print(x)


#Decorators
# Python program to illustrate functions
# can be treated as objects
def shout(text):
    return text.upper()

print(shout('Hello'))
yell = shout
print(yell('Hello'))

def div(a,b):
    if a<b:
        a,b = b,a
    return a/b
a=div
print("The modulus of the two number is : ",round(a(2,4)))

def div(a,b):
    print(a/b)

def smart_div(func):
    print(func)
    def inner(c,d):
        c,d = d,c
        print("HELLO")
        return func(c,d)
    print("hello")
    return inner
div = smart_div
print(div((2,4)))


class sample:
    def getData(self,id ,name):
        self.id = id
        self.name = name
        print(self.id,self.name)
    def getData1(self,id):
        self.id =id
        print(self.id)

    def __init__(self):
        #self.id =id
        #self.name = name
        print("Welcome to Sample Class")
        #print(id, name)

obj = sample()        #sample(3,"Vasanth")
obj.getData1(2)
obj.getData(10,"Guru")


############################# CAR CLASS CATEGORY  #######################################
class car:
    Price = 100000                          #class Variable  -> for accessing we can use classname.variable_name
    def show(self):
        print(" Car Name",self.carname,"\n","Car Type",self.cartype,"\n","Car Color",self.carcolor,"\n","Car Price",self.car_Price)
        print("Car Price for all Cars - self (changed by using class variable with Object name) is ",self.Price)
        print("Car Price for all Cars - (Changed by using class name with class variable) is  ",car.Price)
    def __init__(self,carname,carcolor,cartype,carprice):
        print("Car Details...")
        self.cartype = cartype
        self.carname = carname
        self.carcolor = carcolor
        self.car_Price=carprice
        print("Common Car Price after changing Class variable ",car.Price)
    def show1(self):
        print("Actual Price -(Both should having the same value as Class Variable) ",self.Price,car.Price)
obj = car("Audi A6","Black","Petrol","200000")
obj.show1()
obj.Price=1515
obj.show()

############################ Static Variable ####################################
class Static_variable_Usage:
    static_var = 0

    def __init__(self):
        pass

    def perform(self):
        Static_variable_Usage.static_var +=1
        self.operation = Static_variable_Usage.static_var
        return self.operation
obj = Static_variable_Usage()
print("Initial value of Class Variable",Static_variable_Usage.static_var)
print("After Performing the perform function " ,obj.perform())
print("Final Value of Class Variable " ,Static_variable_Usage.static_var)



class My_Clg:
    clg_name = "KRCT"
    def perform(self):
        return My_Clg.clg_name
obj1 = My_Clg()
obj2 = My_Clg()

print(obj1.perform())
print(obj2.perform())


######################################## Usage of Staticmethod no need to create an object to perform a class operation ######################### 

class Age:
    age=18
    @staticmethod
    def check(n):
        if (Age.age < n):
            return True
        return False
n=int(input("Enter a Age :"))
ck=Age.check(n)
if ck:
    print("Eligible")
else:
    print("Not Eligible")


######################################## Without Using Inheritance we must have inner class #######################################

class Car:
    def __init__(self,name,model):
        self.name = name
        self.model = model
        self.spec = self.Specification()

    def show(self):
        print(self.name,self.model)
        self.spec.show()
    class Specification:
        def __init__(self):
            self.type = "Petrol"
            self.color = "Black Matte Finish"
        def show(self):
            print("Type of the Car is {} and the Color is {} ".format(self.type,self.color))
obj = Car("Audi","A6")
obj.show()


class A:
    def show1(self):
        #super().show1()
        print("A is a Parent Class")
class B:
    def show1(self):
        super().show1()                              #This super() keyword is used to "Check whether it has any other parent class or not
        print("B is a Child Class")
class C(B,A):                                         #Here,it undergoes Multiple Resolution Operation so that It will execute the class B first and then go to class A when the class B contains the super() keyword
    def show1(self):
        super().show1()
        print("C is a Child class of A and B")

class C(B,A):                                        #It will print "B is a Child Class"
    def show1(self):
        print("C is a Child class of A and B")

obj=C()
obj.show1()


class Student:
    def __init__(self,name,age):
        self.name = name
        self.age  = age
    def details(self):
        print(self.name,self.age)
class Student_Address(Student):
    pass
obj = Student_Address("Guru",22)
obj.details()


################################################ Method Overloading ########################################################################
class Student:
    def sum(self,a=None,b=None,c=None):
        s = 0
        if a != None and b != None and c != None :
            s=a+b+c
        elif a != None and b != None :
            s=a+b
        else:
            s=a
        print(type(s))  
        return s
obj=Student()
print(obj.sum())                                    #None
print(obj.sum(5))                                   #5
print(obj.sum(5,6))                                 #11
print(obj.sum(5,6,7))                               #18

"""