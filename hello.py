from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hello')
def hello():
    return "Hello, World!"


@app.route("/")
def index():
    return render_template("index.html")


app.run(port=3000)

