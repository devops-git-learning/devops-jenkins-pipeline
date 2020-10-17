import os
from flask import Flask
app = Flask(__name__)
@app.route("/")
def main():
    return "Welcome to Devops jenkins pipeline learning"
if __name__ == "__main__":

