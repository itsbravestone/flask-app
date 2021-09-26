from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def main():
    return "Hello there!"

@app.route('/dev')
def dev():
    return make_response("Bravestone")

@app.route('/hello')
def dev():
    return make_response("Hello")

app.run(debug=True, port=8080)
