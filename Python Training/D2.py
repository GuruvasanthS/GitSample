"""a=10
print(type(a))
b=1+2j
print(type(b))
print( 10 * "Guru ")
print( "Guru " + "Vasanth")
s="Guruvasanth"
print(s[0:len(s)])                              #Silicing Operator
print(s[::-1])                                  #print the string in reverse
print(s[::])                                    #Print the whole String
str="hello"
print(str)
b=float(a)
print(type(b))
a=10
print(bin(a))                                   #It will return the binary value of a "ob1010" -> 10

l=["Guru",1,"Vasanth",2]
print(*l[0:2])
l.append("Gurushan")
l.insert(4,"GS")
print(l)
l.remove(1)
print("After removing 1 :" ,l)
l.pop()
print("It will remove the last element of an list" ,l)
#l.pop(2)                                       #It will remove the 2nd element in an array
del(l[1:2])
print(l)
l.extend([10,20,30])
print(l)

l1=[20,30,50,10]
l1.sort()
print(l1)
l1.reverse()
print(l1)

tup=(10,20,"Guru")
print(tup)
print(tup[0:])

l1.append(10)
print(l1.count(10))

set={10,10,20}
print(set)

dic={1:"Guru",2:"Vasanth"}
print(dic)
del dic[2]
print(dic)
dic[2] = "Shan"
print(dic)

for i in range(1,len(l1)):
    print(int(l1[i]))

"""
"""a=int(input("Enter a Number1 :"))
b=int(input("Enter a Number2 :"))
print(a+b)
print(a-b)
print(a*b)
print(a/b)

s="mam"
rev=""

for i in range(1,len(s)+1):
    rev+=s[-i]
print(rev)

if s==rev:
    print("Palindrome")
else:
    print("Not a Palindrome")

a1=eval(input())                            #We can directly perfrom Arithmetic Operation "5+5" it prints 10
print(a1)


n=int(input("Enter a number :"))
if n%2==1:
    print("odd")
else:
    print("even")


num=int(input("Enter a Range:"))
n1=0
n2=1 
print(n1,n2,sep='\n')
#print(n2)
for i in range(2,num):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3)


day=int(input("Enter a Number :"))
if day==0:
    print("Sunday")
elif day==1:
    print("Monday")
elif day==2:
    print("Tuesday")
elif day==3:
    print("Wednesday")
elif day==4:
    print("Thursday")
elif day==5:
    print("Friday")
else:
    print("Saturday")
    
def add(n1,n2):
    c=n1+n2
    return c
print(add(1,3))

#############################################     ATM System using FUnction         ###############################################

bal = 1000
def menu():
    n1=int(input("Enter your Choice between 1 to 3 : "))
    if n1==1:
        print(check_bal())
    elif n1==2:
        print("Available balance is :" ,withdraw())
    elif n1==3:
        print("Available balance is :" ,deposit())
    else:
        print("Choose choice between 1 to 3 :")
    exit()

def check_bal():
    global bal
    return bal

def withdraw():
    global bal
    w_amt=int(input("Enter a Amount :"))
    if w_amt < bal:
        bal-=w_amt
        return bal
    else:
        return "Insufficient Balance"

def deposit():
    global bal
    d_amt=int(input("Enter a Amount  : "))
    bal +=d_amt
    return bal

def exit():
    n = input("Do you want to Proceed again y/n : ")
    if (n == 'Y' or n == 'y'):
        menu()
    else:
        print("Thank You...")

n=int(input("Enter a Password : "))
if n==123:
    menu()
else:
    print("OOPS!! Enter a Correct PIN")

for i in range(1,10):
    if (i%2==0):
        pass
    else:
        print(i)
        print("YES")

for i in range(1,10):
    if (i%2==0):
        continue
    else:
        print(i)
        print("YES")
"""

l=[1,2,3]
print(l.pop(0))
del(l[0:3])
print(l)
l.extend([4,5,6])
print(l)