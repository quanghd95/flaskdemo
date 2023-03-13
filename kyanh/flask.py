from flask import Flask 
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

def index():
    return render_template('{user_name}.html')