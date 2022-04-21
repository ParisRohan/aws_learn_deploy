from flask import Flask
app = Flask(__name__)
@app.route('/')

def homepage():
    return '<h1> Hello Rohan :) </h1>'

#use this while deploying
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)