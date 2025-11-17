
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def example():
    return "Hello World!"

@app.route("/reese")
def reese():
    return "Hi Reese!!! Welcome"

@app.route("/raven")
def raven():

    name = request.headers['name']
    file = open("raven.txt", "r", encoding="utf8")
    filetext = file.read()
    return "Hello there " + name + "\n \n" + filetext

@app.route('/addfriend', methods=["POST"])
def add_friend():
    file = open("friends.txt", "a")
    name = request.headers.get("friend")
    file.write(name + "\n")
    return "Friend added!"


if __name__ == "__main__":
    app.run()