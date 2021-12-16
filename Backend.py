
from flask import Flask, redirect, render_template, request, url_for
import mysql.connector

# Flask framework is used to create web applications using python

# creating an object ot host web app using flask api
app = Flask(__name__)

# creating an object to connect to MySQL
mysql = mysql.connector.connect(host = 'Neha0077.mysql.pythonanywhere-services.com', user = 'Neha0077', password = 'admin123', database = 'Neha0077$default')

# creating cursor object to execute mysql queries in python code
mycursor = mysql.cursor()


# variable to store which user is currently logged in
user = ""

# routing function to '/' page
@app.route('/', methods=['GET', 'POST'])
def Login():

    global user
    global password

    if(request.method == 'POST'):

        # fetch details from the form
        Input_from_user = []
        for x in request.form:
            Input_from_user.append(str(request.form[x]))

        user = Input_from_user[0]
        password = Input_from_user[1]

        # fetching details from the sql server to check whether this user is signed up or not
        sql_Select_Query = "Select UserName,password from UserInput"

        mycursor.execute(sql_Select_Query)

        myresult = mycursor.fetchall()

        for x in myresult:

            if((user in x) and (password in x)):
                return "Successfully logged in"
            else:
                return "Invalid username or password!"

    # Display a login form

    return render_template('Login_page.html')

@app.route('/SignUp', methods=['GET', 'POST'])
def Signup():

    # checking if data is inputted
    if request.method == 'POST':

      # check the data for any errors
      for x in request.form:
         print(request.form[x], end=" : ")
         print(type(request.form[x]))

      # saving sql command in a variable
      sql_Insert_Query = "INSERT INTO UserInput (FirstName,LastName, MailId, PhoneNo, Age, Gender,UserName, password ) VALUES (%s, %s,%s, %s, %s, %s, %s,%s)"

      # fetching data from HTML form to python code and storing it in a list
      Input_From_User = []
      for x in request.form:
         Input_From_User.append(str(request.form[x]))


      # Creating a table for user to store all the transactions
      sql_Create_table_query = "Create table {}(Amount varchar(30), TUse varchar(30), DTime varchar(30))".format(str(request.form['UserName']))

      # typecasting from list to tuple
      Input_From_User = tuple(Input_From_User)

      # if UserName is not present in the Database then register it in the database
      mycursor.execute(sql_Insert_Query, Input_From_User)

      # Also creating a new table for storing transactions in sql table
      mycursor.execute(sql_Create_table_query)

      mysql.commit()
      return "Account registered successfully!!!"

      print(mycursor.rowcount, "record inserted.")

    return render_template("User_input.html")

'''
   This line takes transactions from user, stores them in a database and displays them which
   transactions they have done on that page itself
'''
Transactions = []
Rows = []
@app.route('/Transactions',methods=['GET','POST'])
def Inputting_transactions():

    # storing sql command in variable
    sql = "INSERT INTO transactions(Amount, TUse, DTime) VALUES(%s, %s, %s)"

    # checking if user wants to view the website for the first time
    if request.method == "GET":

        # rendering the template
        return render_template("Transaction_form_using_table.html", Transactions=Transactions)

    # fetching data from html and storing it in a variable
    Rows = []
    for x in request.form:
        Rows.append(str(request.form[x]))

    print(Rows)

    Transactions.append(Rows)
    # Typecasting Rows list to tuple
    Rows = tuple(Rows)

    # executing mysql command
    mycursor.execute(sql, Rows)
    mysql.commit()

    # reopening the website again
    return redirect(url_for("Inputting_transactions"))



