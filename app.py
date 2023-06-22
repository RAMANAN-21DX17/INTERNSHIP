# Store this code in 'app.py' file
 
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import json
 
 
app = Flask(__name__)
 
global account ,room, room1, room2, room3,room4,room5, meet
app.secret_key = 'RAMANAN'
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'fide25610279'
app.config['MYSQL_DB'] = 'makemymeeting'
 
mysql = MySQL(app)
 
@app.route('/')
def home():
    msg = ''
    return render_template('Index.html', msg = msg)

@app.route('/login', methods =['GET', 'POST'])
def login():
    print ("login")
    msg = " "
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        global account ,room, room1, room2, room3,room4,room5
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
            if account["positon"] == "Employee":
                cursor.execute('SELECT name,time1,time2,time3,time4,time5 FROM room WHERE company = % s', (account['company'], ))
                room = cursor.fetchall()
                print(room)
                room1 = room[0] 
                room2 = room[1]
                room3 = room[2]
                room4 = room[3]
                room5 = room[4]
                return render_template('E-HOMEPAGE.html',room1 = room1,room2 = room2,room3 =room3,room4 = room4,room5 = room5 )
            else:
                return render_template('A-HOMEPAGE.html',msg =msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('LOGIN.html') 
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
            if usertype == 'Employee':
                cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s, % s, % s, % s)', (username, password, email, location, company, usertype, ))
                mysql.connection.commit()
                msg = 'You have successfully registered !'
                for i in range(0,5):
                    cursor.execute('insert into meetings values (%s ,null,null,null,null,null)',(username,))
                    mysql.connection.commit()
                return render_template('LOGIN.html', msg = msg)
            elif usertype == 'Admin':
                cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s, % s, % s, % s)', (username, password, email, location, company, usertype, ))
                mysql.connection.commit()
                cursor.execute('INSERT INTO company VALUES ( % s, % s, 0)', ( company, location, ))
                mysql.connection.commit()
                i = 0
                for i in range(0,5):
                    room_name = "ROOM "+str(i+1)
                    cursor.execute('insert into room values (%s ,%s ,"available","available","available","available","available")',(company,room_name,))
                    mysql.connection.commit()
                    cursor.execute('insert into meetings values (%s ,null,null,null,null,null)',(username,))
                    mysql.connection.commit()
                msg = 'You have successfully registered !'
                return render_template('LOGIN.html', msg = msg)
    return render_template('SIGNUP.html', msg = msg)

@app.route('/time11')
def time11():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('update room set time1 = null where company = %s and name = %s',(account['company'],room1['name'],))
    mysql.connection.commit()
    cursor.execute('update meetings set meeting1 = %s where user = %s',(room1['name'],account['username'],))
    mysql.connection.commit()
    return redirect(url_for('meetings'))
@app.route('/time12')
def time12():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('update room set time2 = null where company = %s and name = %s',(account['company'],room1['name'],))
    mysql.connection.commit()
    cursor.execute('update meetings set meeting2 = %s where user = %s',(room1['name'],account['username'],))
    mysql.connection.commit()
    return redirect(url_for('meetings'))
@app.route('/time13')
def time13():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('update room set time3 = null where company = %s and name = %s',(account['company'],room1['name'],))
    mysql.connection.commit()
    cursor.execute('update meetings set meeting3 = %s where user = %s',(room1['name'],account['username'],))
    mysql.connection.commit()
    return redirect(url_for('meetings'))
@app.route('/time14')
def time14():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('update room set time4 = null where company = %s and name = %s',(account['company'],room1['name'],))
    mysql.connection.commit()
    cursor.execute('update meetings set meeting4 = %s where user = %s',(room1['name'],account['username'],))
    mysql.connection.commit()
    return redirect(url_for('meetings'))
@app.route('/time15')
def time15():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('update room set time5 = null where company = %s and name = %s',(account['company'],room1['name'],))
    mysql.connection.commit()
    cursor.execute('update meetings set meeting5 = %s where user = %s',(room1['name'],account['username'],))
    mysql.connection.commit()
    return redirect(url_for('meetings'))

@app.route('/time21')
def time21():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('update room set time1 = null where company = %s and name = %s',(account['company'],room2['name'],))
    mysql.connection.commit()
    cursor.execute('update meetings set meeting1 = %s where user = %s',(room2['name'],account['username'],))
    mysql.connection.commit()
    return redirect(url_for('meetings'))
@app.route('/time22')
def time22():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('update room set time2 = null where company = %s and name = %s',(account['company'],room2['name'],))
    mysql.connection.commit()
    cursor.execute('update meetings set meeting2 = %s where user = %s',(room2['name'],account['username'],))
    mysql.connection.commit()
    return redirect(url_for('meetings'))
@app.route('/time23')
def time23():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('update room set time3 = null where company = %s and name = %s',(account['company'],room2['name'],))
    mysql.connection.commit()
    cursor.execute('update meetings set meeting3 = %s where user = %s',(room2['name'],account['username'],))
    mysql.connection.commit()
    return redirect(url_for('meetings'))
@app.route('/time24')
def time24():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('update room set time4 = null where company = %s and name = %s',(account['company'],room2['name'],))
    mysql.connection.commit()
    cursor.execute('update meetings set meeting4 = %s where user = %s',(room2['name'],account['username'],))
    mysql.connection.commit()
    return redirect(url_for('meetings'))
@app.route('/time25')
def time25():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('update room set time5 = null where company = %s and name = %s',(account['company'],room2['name'],))
    mysql.connection.commit()
    cursor.execute('update meetings set meeting5 = %s where user = %s',(room2['name'],account['username'],))
    mysql.connection.commit()
    return redirect(url_for('meetings'))

@app.route('/time31')
def time31():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('update room set time1 = null where company = %s and name = %s',(account['company'],room3['name'],))
    mysql.connection.commit()
    cursor.execute('update meetings set meeting1 = %s where user = %s',(room3['name'],account['username'],))
    mysql.connection.commit()
    return redirect(url_for('meetings'))
@app.route('/time32')
def time32():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('update room set time2 = null where company = %s and name = %s',(account['company'],room3['name'],))
    mysql.connection.commit()
    cursor.execute('update meetings set meeting2 = %s where user = %s',(room3['name'],account['username'],))
    mysql.connection.commit()
    return redirect(url_for('meetings'))
@app.route('/time33')
def time33():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('update room set time3 = null where company = %s and name = %s',(account['company'],room3['name'],))
    mysql.connection.commit()
    cursor.execute('update meetings set meeting3 = %s where user = %s',(room3['name'],account['username'],))
    mysql.connection.commit()
    return redirect(url_for('meetings'))
@app.route('/time34')
def time34():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('update room set time4 = null where company = %s and name = %s',(account['company'],room3['name'],))
    mysql.connection.commit()
    cursor.execute('update meetings set meeting4 = %s where user = %s',(room3['name'],account['username'],))
    mysql.connection.commit()
    return redirect(url_for('meetings'))
@app.route('/time35')
def time35():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('update room set time5 = null where company = %s and name = %s',(account['company'],room3['name'],))
    mysql.connection.commit()
    cursor.execute('update meetings set meeting5 = %s where user = %s',(room3['name'],account['username'],))
    mysql.connection.commit()
    return redirect(url_for('meetings'))
@app.route('/time41')
def time41():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('update room set time1 = null where company = %s and name = %s',(account['company'],room4['name'],))
    mysql.connection.commit()
    cursor.execute('update meetings set meeting1 = %s where user = %s',(room4['name'],account['username'],))
    mysql.connection.commit()
    return redirect(url_for('meetings'))
@app.route('/time42')
def time42():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('update room set time2 = null where company = %s and name = %s',(account['company'],room4['name'],))
    mysql.connection.commit()
    cursor.execute('update meetings set meeting2 = %s where user = %s',(room4['name'],account['username'],))
    mysql.connection.commit()
    return redirect(url_for('meetings'))
@app.route('/time43')
def time43():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('update room set time3 = null where company = %s and name = %s',(account['company'],room4['name'],))
    mysql.connection.commit()
    cursor.execute('update meetings set meeting3 = %s where user = %s',(room4['name'],account['username'],))
    mysql.connection.commit()
    return redirect(url_for('meetings'))
@app.route('/time44')
def time44():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('update room set time4 = null where company = %s and name = %s',(account['company'],room4['name'],))
    mysql.connection.commit()
    cursor.execute('update meetings set meeting4 = %s where user = %s',(room4['name'],account['username'],))
    mysql.connection.commit()
    return redirect(url_for('meetings'))
@app.route('/time45')
def time45():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('update room set time5 = null where company = %s and name = %s',(account['company'],room4['name'],))
    mysql.connection.commit()
    cursor.execute('update meetings set meeting5 = %s where user = %s',(room4['name'],account['username'],))
    mysql.connection.commit()
    return redirect(url_for('meetings'))
@app.route('/time51')
def time51():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('update room set time1 = null where company = %s and name = %s',(account['company'],room5['name'],))
    mysql.connection.commit()
    cursor.execute('update meetings set meeting1 = %s where user = %s',(room5['name'],account['username'],))
    mysql.connection.commit()
    return redirect(url_for('meetings'))
@app.route('/time52')
def time52():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('update room set time2 = null where company = %s and name = %s',(account['company'],room5['name'],))
    mysql.connection.commit()
    cursor.execute('update meetings set meeting2 = %s where user = %s',(room5['name'],account['username'],))
    mysql.connection.commit()
    return redirect(url_for('meetings'))
@app.route('/time53')
def time53():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('update room set time3 = null where company = %s and name = %s',(account['company'],room5['name'],))
    mysql.connection.commit()
    cursor.execute('update meetings set meeting3 = %s where user = %s',(room5['name'],account['username'],))
    mysql.connection.commit()
    return redirect(url_for('meetings'))
@app.route('/time54')
def time54():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('update room set time4 = null where company = %s and name = %s',(account['company'],room5['name'],))
    mysql.connection.commit()
    cursor.execute('update meetings set meeting4 = %s where user = %s',(room5['name'],account['username'],))
    mysql.connection.commit()
    return redirect(url_for('meetings'))
@app.route('/time55')
def time55():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('update room set time5 = null where company = %s and name = %s',(account['company'],room5['name'],))
    mysql.connection.commit()
    cursor.execute('update meetings set meeting5 = %s where user = %s',(room5['name'],account['username'],))
    mysql.connection.commit()
    return redirect(url_for('meetings'))

@app.route('/meetings')
def meetings():
    print("meetings")
    global meet
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM meetings WHERE user = %s', (account['username'], ))
    meet = cursor.fetchone()
    print(meet)
    return render_template('meetings.html', meet = meet)

@app.route('/remove1')
def remove1():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('update meetings set meeting1 = null where user = %s',(account['username'],))
    mysql.connection.commit()
    cursor.execute('update room set time1 = "available" where company = %s and name = %s',(account['company'],room1['name'],))
    mysql.connection.commit()
    cursor.execute('SELECT * FROM meetings WHERE user = %s', (account['username'], ))
    meet = cursor.fetchall()
    return render_template('meetings.html', meet = meet)

@app.route('/remove2')
def remove2():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('update meetings set meeting2 = null where user = %s',(account['username'],))
    mysql.connection.commit()
    cursor.execute('update room set time2 = "available" where company = %s and name = %s',(account['company'],room2['name'],))
    mysql.connection.commit()
    cursor.execute('SELECT * FROM meetings WHERE user = %s', (account['username'], ))
    meet = cursor.fetchall()
    return render_template('meetings.html', meet = meet)

@app.route('/remove3')
def remove3():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('update meetings set meeting3 = null where user = %s',(account['username'],))
    mysql.connection.commit()
    cursor.execute('update room set time3 = "available" where company = %s and name = %s',(account['company'],room3['name'],))
    mysql.connection.commit()
    cursor.execute('SELECT * FROM meetings WHERE user = %s', (account['username'], ))
    meet = cursor.fetchall()
    return render_template('meetings.html', meet = meet)

@app.route('/remove4')
def remove4():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('update meetings set meeting4 = null where user = %s',(account['username'],))
    mysql.connection.commit()
    cursor.execute('update room set time4 = "available" where company = %s and name = %s',(account['company'],room4['name'],))
    mysql.connection.commit()
    cursor.execute('SELECT * FROM meetings WHERE user = %s', (account['username'], ))
    meet = cursor.fetchall()
    return render_template('meetings.html', meet = meet)

@app.route('/remove5')
def remove5():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('update meetings set meeting5 = null where user = %s',(account['username'],))
    mysql.connection.commit()
    cursor.execute('update room set time5 = "available" where company = %s and name = %s',(account['company'],room5['name'],))
    mysql.connection.commit()
    cursor.execute('SELECT * FROM meetings WHERE user = %s', (account['username'], ))
    meet = cursor.fetchall()
    return render_template('meetings.html', meet = meet)