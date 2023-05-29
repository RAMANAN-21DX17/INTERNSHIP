from flask import Flask, render_template, request

app = Flask(login.html)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Add your authentication logic here
    # For simplicity, let's assume the username is "admin" and password is "password"
    if username == 'admin' and password == 'password':
        return 'Login successful!'
    else:
        return 'Invalid credentials.'

if login.html == '_main_':
    app.run()