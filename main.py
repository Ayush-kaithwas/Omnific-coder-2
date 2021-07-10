from flask import Flask, render_template, request, session, redirect, flash
from flask_sqlalchemy import SQLAlchemy
import json
from flask import *


with open('config.json', 'r') as c:
    params = json.load(c)["params"]


local_server = True
app = Flask(__name__)
app.secret_key = 'super-secret-key'


db = SQLAlchemy(app)  # Initialization

# -----------------------------Home Page---------------------------
@app.route('/')
def home():
    return render_template('index.html', params=params)

# -------------------------Courses Page---------------------------
@app.route('/course')
def course():
    return render_template('course.html', params=params)

# -------------------------About Page-----------------------------------
@app.route('/about')
def about():
    return render_template('about.html', params=params)

# -------------------------Contact Page-----------------------------------
@app.route('/contact')
def contact():
    return render_template('contact.html', params=params)

# -------------------------Blog Page-----------------------------------
@app.route('/blog')
def blog():
    return render_template('blog.html', params=params)

# --------------------------login Page and Dashboard Page---------------------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if ('user' in session and session['user'] == params['admin_user']):
        return render_template('dashboard.html', params=params)

    if (request.method == "POST"):
        username = request.form.get('uname')
        userpass = request.form.get('password')
        if (username == params['admin_user'] and userpass == params['admin_password']):
            # set the session variable
            session['user'] = username
            return render_template('dashboard.html', params=params)
        else:
            flash('Wrong Id or Password')

    return render_template('login.html', params=params)



@app.route("/logout")
def logout():
    session.pop('user')
    return redirect('/login')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0' )
