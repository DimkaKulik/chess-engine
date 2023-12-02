from flask import Flask

app = Flask(__name__)

@app.route("/hello_world")
def hello_world():
    return '<h1>Hello World</h1>'
