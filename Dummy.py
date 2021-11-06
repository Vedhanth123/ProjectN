
from flask import Flask, render_template, request
import mysql.connector

# creating an object ot host web app using flask api
app = Flask(__name__)


# creating an object to connect to MySQL
mysql = mysql.connector.connect(host='Neha0077.mysql.pythonanywhere-services.com',
                                user='Neha0077', password='admin123', database='Neha0077$default')

# creating cursor object to execute mysql queries in python code
mycursor = mysql.cursor()

# routing hello_world function to '/' page


@app.route('/', methods=['GET', 'POST'])
def hello_world():

    if request.method == 'POST':

        # check the data for any errors
        for x in request.form:
            print(request.form[x], end=" : ")
            print(type(request.form[x]))

        # saving sql command in a variable
        sql_Insert_Query = "INSERT INTO UserInput (FirstName,LastName, MailId, PhoneNo, Age, Gender,UserName, password, ConfirmPassword ) VALUES (%s, %s, %s,%s, %s, %s, %s, %s,%s)"

        # fetching data from HTML form to python code and storing it in a list
        Input_From_User = []
        for x in request.form:
            Input.append(str(request.form[x]))

        # typecasting from list to tuple
        Input_From_User = tuple(Input_From_User)

        # checking if UserName entered is already present in the Database
        sql_Select_Query = "Select UserName from UserInput where UserName in '%s'"

        mycursor.execute(sql_Select_Query, (request.form['UserName'],))

        if(len(records) == 0):
            return "UserName is registered Successfully!!!"
        else:
            return "UserName is already in use"

        # mycursor.execute(sql, Input_From_User)

        # mysql.commit()


        print(mycursor.rowcount, "record inserted.")

    return render_template("User_input.html")
