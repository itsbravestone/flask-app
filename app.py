from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def main():
    return "Hello World!!!"

@app.route('/dev')
def dev():
    return make_response("Bravestone")

@app.route('/hello')
def hello():
    return make_response("Hello there")

app.run(debug=True, port=8080)
