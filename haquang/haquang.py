from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('haquang.html')

@app.route('/list_user/')
def list_user():
    users = [
        {"name": "quang", "href": "https://github.com/quanghd95/flaskdemo"},
        {"name": "ha", "href": "https://github.com/quanghd95/Python4KId"},
        {"name": "xxxx", "href": "https://github.com/quanghd95/Python4KId"}
    ]

    a = "Hello world"
    return render_template('list_user.html', users = users, a = a)

