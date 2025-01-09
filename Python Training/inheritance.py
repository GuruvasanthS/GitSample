#D3
#Multiple Inheritance
class A:
    def show1(self):
        #super().show1()
        print("A is a Parent Class")
class B:
    def show1(self):
        #super().show1()                              #This super() keyword is used to "Check whether it has any other class or not
        print("B is a Child Class")
class C(B,A):                                         #Here,it undergoes Multiple Resolution Operation so that It will execute the class B first and then go to class A when the class B contains the super() keyword
    def show1(self):
        super().show1()
        print("C is a Child class of A and B")
obj=C()
obj.show1()

print(C.__mro__)                                     #Method Resolution Operation