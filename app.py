from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

@app.route('/')
def welcome():
        return render_template('paxmate.html') # renders teh template

@app.route('/login')
def login():
        return render_template('login.html')

if __name__ == '__main__':
        app.run('localhost', 5555, debug = True)
