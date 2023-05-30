# Store this code in 'app.py' file
 
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
 
 
app = Flask(__name__)
 
 
app.secret_key = 'RAMANAN'
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Ramanan1836@'
app.config['MYSQL_DB'] = 'makemymeeting'
 
mysql = MySQL(app)
 
@app.route('/')
def home():
    msg = ''
    return render_template('Index.html', msg = msg)
@app.route('/login', methods =['GET', 'POST'])
def login():
    msg = ''
    print ("login")
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        print ("requested")
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = % s AND password = % s', (username, password, ))
        print ("cursor")
        account = cursor.fetchone()
        print ("fetched")
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            msg = 'Logged in successfully !'
            if account["positon"] == "Employee":
                return render_template('E-HOMEPAGE.html', msg = msg)
            else:
                return render_template('A-HOMEPAGE.html',msg =msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('LOGIN.html', msg = msg)
 
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))
 
@app.route('/register', methods =['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST':
        usertype = request.form['usertype']
        username = request.form['username']
        company = request.form['company']
        location = request.form['location']
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = % s', (username, ))
        account = cursor.fetchone()
        cursor.execute('SELECT * FROM accounts WHERE company = % s', (company, ))
        com = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not username or not password or not email or not location or not company:
            msg = 'Please fill out the form !'
        elif usertype == 'Admin' and com:
            msg = 'Your Company is already registered!!'
        else:
            cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s, % s, % s, % s)', (username, password, email, location, company, usertype, ))
            mysql.connection.commit()
            msg = 'You have successfully registered !'
            return render_template('LOGIN.html', msg = msg)
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('SIGNUP.html', msg = msg)