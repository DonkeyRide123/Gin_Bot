# Imports flask (a webserver module)
from flask import Flask

# Imports threading (a module that runs the code asynchronously)
from threading import Thread

# Creates a server with Flask
app = Flask("")


# Sets the home page to "I'm alive"
@app.route("/")
def home():
    return "I'm alive"


# Runs the app
def run():
    app.run(host="0.0.0.0", port=8080)


# Keeps the web server alive
def keep_alive():
    t = Thread(target=run)
    t.start()
