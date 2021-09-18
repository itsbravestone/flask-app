from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return "Hello there!"

@app.route('/dev')
def dev():
    return "Steve"

app.run(debug=True)
