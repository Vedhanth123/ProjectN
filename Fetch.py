import mysql.connector


# creating an object to connect to MySQL
mysql = mysql.connector.connect(host = 'localhost', user = 'root', password = 'admin', database = 'google')

# creating cursor object to execute mysql queries in python code
mycursor = mysql.cursor()

mycursor.execute("Select * from UserInput")

for x in mycursor.fetchall():
    print(x)
