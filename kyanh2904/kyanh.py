from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        return render_template("kyanh.html", name=name)
    else:
        return render_template("kyanh.html")