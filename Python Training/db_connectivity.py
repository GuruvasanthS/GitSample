#CRUD operations
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password ="root",
    database = "python_be"
)
mycursor = mydb.cursor()
"""mycursor.execute("CREATE TABLE students(name varchar(255),age int(10))")
mycursor.execute("INSERT INTO students (name,age) values (%s,%s)",("Guru",22))
mydb.commit()
print(mycursor.rowcount,"Record Inserted")
insert_st ="INSERT INTO students (name,age) values (%(name)s,%(age)s)"
val = [{"name":"Vasanth","age":"23"}, {"name":"GV","age":"22"}]
#Insert Data in a table
mycursor.executemany(insert_st,val)
#fetch Data in a table
mycursor.execute("SELECT * from students")
data_in_table = mycursor.fetchall()
for i in data_in_table:
    print(i)"""
d=[{"age":22},{"age":21}]
for i in d:
    print(i)
    x=i["age"]
    mycursor.execute("Select * from students where age = {} " .format(x))
    records = mycursor.fetchall()
    print(records)
mydb.commit()


