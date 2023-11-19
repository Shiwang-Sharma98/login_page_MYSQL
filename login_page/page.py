import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user="abc",
    password="password",
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE if not exists user_data")
mycursor.execute("CREATE TABLE if not exists user_data.user_table(name VARCHAR(50),pass VARCHAR(50))")
from flask import Flask,request,render_template
app = Flask(__name__)

def exists_name(l,name):
    for i in range(len(l)):
        if l[i][0] == name:
            return True
    return False

def exists_pass(l,password):
    for i in range(len(l)):
        if l[i][1] == password:
            return True
    return False

@app.route("/")
def login_page():
    return render_template("index.html")

@app.route("/task",methods=["POST"])
def main():
    name = request.form['user']
    Password = request.form['user_pass']
    mycursor.execute("select * from user_data.user_table")
    l = []
    for i in mycursor.fetchall():
        l.append(list(i))
    
    if exists_name(l,name):
        if exists_pass(l,Password):
            return f'login successful'
    elif exists_name(l,name):
        return f'name does not exists'
    else :
        return f'you are not yet registored'
    

@app.route("/register.php")
def main1():
    return render_template("index1.html")

@app.route("/task1",methods=["POST"])
def main2():
    name = request.form['user']
    Password = request.form['user_pass']
    mycursor.execute("INSERT INTO user_data.user_table (name, pass) VALUES (%s, %s)", (name, Password))
    mydb.commit()
    return f'successfull registered'


if __name__=='__main__':
     app.run(host='0.0.0.0', port=5000)
