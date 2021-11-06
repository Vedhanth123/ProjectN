import mysql.connector

# creating an object of mysql.connector.connect()
mysql = mysql.connector.connect(host = 'localhost', user = 'root', password = 'admin', database = 'google')

# creating cursor object to execute mysql queries in python code
mycursor = mysql.cursor()

# taking email as input from user and checking whether that email is already present in database or not

email = input("Enter your email address: ")
email = str(email)

mysql_query = 'select MailId from UserInput where MailId = %s'

# this is used to execute sql queries in python
mycursor.execute(mysql_query, (email, ))

records = mycursor.fetchall()

if(len(records) == 0):
    print("Your email has been registered")
else:
    print("Your email has already been used")
mysql.commit()
