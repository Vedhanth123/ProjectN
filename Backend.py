# Enter the data into the HTML form

from flask import Flask, redirect, render_template, request, url_for
import mysql.connector

# creating an object to host web app using flask api
app = Flask(__name__)

# creating an object to connect to MySQL
mysql = mysql.connector.connect(host = 'localhost', user = 'root', password = 'admin', database = 'google')

# creating cursor object to execute mysql queries in python code
mycursor = mysql.cursor()

# routing hello_world function to '/' page
# @app.route('/', methods=['GET', 'POST'])
# def Login_Page():

#    if request.method == 'POST':

#       # check the data for any errors
#       for x in request.form:
#          print(request.form[x], end=":")
#          print(type(request.form[x]))
          
#       # saving sql command in a variable
#       sql = "INSERT INTO UserInput (FirstName,LastName, MailId, PhoneNo, Age, Gender, UserName,password, confirm_password) VALUES (%s, %s, %s, %s, %s, %s,%s, %s, %s)"

#       # fetching data from HTML form to python code and storing it in a list
#       Input = []
#       for x in request.form:
#          Input.append(str(request.form[x]))
      
#       if(len(Input) != 0):
            
#          # typecasting from list to tuple
#          Input = tuple(Input)

#          # executing sql query
#          mycursor.execute(sql, Input)

#          # saving changes in mysql database
#          mysql.commit()

      
#    return render_template("User_input.html")

'''
   This line takes transactions from user, stores them in a database and displays them which
   transactions they have done on that page itself
'''
Transactions = []
Rows = []
@app.route('/',methods=['GET','POST'])
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
   
   Transactions.append(Rows)
   # Typecasting Rows list to tuple
   Rows = tuple(Rows)

   # executing mysql command
   mycursor.execute(sql, Rows)
   mysql.commit()

   # reopening the website again
   return redirect(url_for("Inputting_transactions"))


if __name__ == '__main__':
   app.run(host='localhost', port=8080, debug=True)