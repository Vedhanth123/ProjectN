# Enter the data into the HTML form

from flask import Flask, render_template, request
import mysql.connector

# creating an object ot host web app using flask api
app = Flask(__name__)


# creating an object to connect to MySQL
mysql = mysql.connector.connect(host = 'localhost', user = 'root', password = 'admin', database = 'google')

# creating cursor object to execute mysql queries in python code
mycursor = mysql.cursor()

# routing hello_world function to '/' page
@app.route('/', methods=['GET', 'POST'])
def hello_world():

   if request.method == 'POST':

      # check the data for any errors
      for x in request.form:
         print(request.form[x], end=":")
         print(type(request.form[x]))
          
      # saving sql command in a variable
      sql = "INSERT INTO UserInput (FirstName,LastName, MailId, PhoneNo, Age, Gender ,Password) VALUES (%s, %s, %s, %s, %s, %s)"

      # fetching data from HTML form to python code and storing it in a list
      Input = []
      for x in request.form:
         Input.append(str(request.form[x]))
      
      
      # typecasting from list to tuple

      Input = tuple(Input)
      mycursor.execute(sql, Input)

      mysql.commit()
      

      print(mycursor.rowcount, "record inserted.")

   return render_template("User_input.html")


if __name__ == '__main__':
   app.run(host='localhost', port=8080, debug=True)