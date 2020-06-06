from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__)

@app.route('/')
def index():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'tanay':
        session['logged_in'] = True
    else:
        flash('Wrong password!')
    return index()

@app.route('/area', methods=['POST', 'GET'])
def area():
    if request.method == 'POST':
        sideA = int(request.form['sidea'])
        sideB = int(request.form['sideb'])
        area = sideA * sideB
        return render_template('area.html', area=area)
    else:
        return render_template('area.html')

@app.route('/welcome/<name>')
def welcome(name):
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('welcome_page.html', name=name)

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=5000)