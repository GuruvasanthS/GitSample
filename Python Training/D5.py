##################################################### DJANGO ################################################################
#c:/users/django/Project1
"""
d = { "brand": "Ford",
  "model": "Mustang",
  "year": 1964
    }

x=d.get("brand")
print(x)

#Displays the key elements of a Dictionary
y=d.keys()
print(y)

#Adding a key value pair element in a dictionary
#Method 1
d['color'] = "White"
print(d)
print(y)
#Method 2
up = {"Specs":"High End"}
d.update(up)
print(d)

#List all the values in a dictionary
d.values()
print(d)

#We can't use append in dictionary
#for i in d:
#    d.append(["release"]["2022"])
l1=["guru","vasanth"]
l2=[23,22,24]

new_dict_lam = dict(map(lambda i,j : (i,j) , l1,l2))
print("Dictionary using Lambda : ",new_dict_lam)

new_dict = {l1[i]:l2[i] for i in range(len(l1))}
print("Converting Two List into Dictionary : ",new_dict)

#sorted by using value in dictionary
new_dict1 = dict(sorted(new_dict.items(),key = lambda item : item[1] ))
print("Based on Values : ",new_dict1)

new_dict2 = dict(sorted(new_dict.items()))
print("Based on Keys : ",new_dict2)

new_dict1 = dict(sorted(new_dict.items(),key = len ))
print("Based on length of the keys : ",new_dict1)



dict1 = {"Guru" : {"Age" :22,"Dept":"IT"},
        "Vasanth" :{"Age":23,"Dept":"AI"}
        }
print(dict)

#Sorting the elements in nested dictionary
new_nest_dic = dict(sorted(dict1.items(),key = lambda i:i[1]["Dept"]))
print(new_nest_dic)

"""



"""#######################################         PYTHON ASSESSMENT - 1 QUESTION              #####################################################
#3.calculate the total cost of all the products sold,total quantity,Highest sale and Lowest sale

def is_valid_product(products):
    return products['price'] >= 0 and products['quantity'] >=0

def calculate_product(products1):
    quantity = 0
    sum_p = 0
    max_p = 0
    min_p = float('inf')             # Use infinity for initial minimum comparison
    #print(min_p)                     #inf type is float
    #for i in products:
    #   if is_valid_product((i)):
    valid_p = [i for i in products if is_valid_product(i)]
    for i in valid_p:
        sum_p  += i['price'] * i['quantity']
        quantity += i['quantity']

    for i in valid_p:
        high_p = i['price'] * i['quantity']
        if max_p < high_p:
            max_p = high_p
        low_p = i['price'] * i['quantity']
        if min_p > low_p:
            min_p = low_p
    for i in valid_p:
        if min_p ==  i['price'] * i['quantity']:
            low_p = i
        if max_p ==  i['price'] * i['quantity']:
            high_p = i
    return sum_p,quantity,high_p,low_p

products = [ {'name': 'laptop', 'price': 1200, 'quantity': 3},
             {'name': 'Mouse', 'price': 25, 'quantity': 10}, {'name': 'Keyboard', 'price': 45, 'quantity': 5},
            {'name': 'Monitor', 'price': 300, 'quantity': 2}, {'name': 'Headphones', 'price': 100, 'quantity': 7}]

s_p,q_p,h_p,l_p = calculate_product(products)
print("Total cost of all the products sold : " ,s_p)
print("Total Quantity of product sold : ",q_p)
print("Highest Sale is :",h_p)
print("Lowest Sale is :",l_p)"""


#######################################################################################################################
#4.

books = [   {'title': "The Great Gatsby", 'author': "F.Scott Fitzgerald", 'publication _date': 1925},
            {'title': "To Kill a Mockingbird", 'author': 'Harpe Lee', 'publication_date': 1960},
            {'title': '1984', 'author': 'George Orwell','publication _date': 1949},
            {'title': "Pride and Prejudice",'author': 'Jane Austen' ,'publication _date': 1813}
        ]
print(books)

def menu():
    print("1.Add a New Book")
    print("2.Remove a Book")
    print("""3.Search for Book either with "Title" or "Author" """)
    print("4.Sort and Display the list of Books")
    n = int(input("Enter Your Choice : "))
    if n == 1:
        print(add_book(books))
    elif n == 2:
        print(remove_book(books))
    elif n == 3:
        search_book(books)
    elif n == 4:
        sort_book(books)
    else:
        print("Enter a Valid Choice ")
    exit()

def add_book(books):
    n=int(input("How many numbers of books to be added : "))
    for _ in range(n):
        title = input("Enter a Title of  a Book : ")
        author = input("Enter a Author of a Book : ")
        date_book = int(input("Enter a Publication Date of a Book : "))
        new_book = { 'title': title, 'author': author, 'date': date_book }
        books.append(new_book)
    #books['title'] = title
    #books ['author'] = author
    #books['date'] = date_book
    return books
def remove_book(books):
    t1 = input("Enter a Title of a Book to Remove : ")
    new_book = {'title':t1}
    print(new_book)
    del books[t1]
    print(books)
    #books.remove(new_book)
    return books
def search_book(books):
    s1 = input("Enter a Title of a Book to Search : ")
    for i in books:
        print(i)
        if s1 in i:
            print(i)
            print("The Searched Book is : ",i)
def sort_book(books):
    pass
def exit():
    n1 = input("Do you want to Proceed again y/n : ")
    if (n1 == 'Y' or n1 == 'y'):
        menu()
    else:
        print("Thank You...")

menu()
