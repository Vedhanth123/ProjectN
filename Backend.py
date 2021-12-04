# Enter the data into the HTML form

from flask import Flask, render_template, request
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

@app.route('/',methods=['GET','POST'])
def Inputting_transactions():

   # create a html page which take transactions in the form of a table

   # New row is added in the table if user clicks on add more button
   # THis functionality is accomplished by using javascript in html code to add new rows in a table using javascript event handling concept.

   if request.method == "POST":

      print("")
      print("Transaction data: ")
      print("")
      for x in request.form:
         print(request.form[x], end=":")
         print(type(request.form[x]))

         
         
   else:
      return render_template("Transaction_form_using_table.html")

   pass
if __name__ == '__main__':
   app.run(host='localhost', port=8080, debug=True)