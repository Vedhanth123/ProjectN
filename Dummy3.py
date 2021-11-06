import mysql.connector

# creating an object of mysql.connector.connect()
mysql = mysql.connector.connect(host = 'localhost', user = 'root', password = 'admin', database = 'google')

# creating cursor object to execute mysql queries in python code
mycursor = mysql.cursor()

name = input("Enter your name: ")

name = str(name)
sql_query = "select UserName from UserInput2 where UserName = %s"

mycursor.execute(sql_query, (name,))

record = mycursor.fetchall()

if(len(record) == 0):
    print("Empty list")
else:
    print("Your name is already present in the list")