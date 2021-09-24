from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def main():
    return "Hello there!"

@app.route('/dev')
def dev():
    return "Bravestone"

app.run(debug=True, port=8080)
