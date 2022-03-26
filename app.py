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
    hello = "hey there"
    return make_response("Hello there", hello)

@app.route('/hey')
def hey():
    wish = "Happy New Year 2022"
    return make_response("wish", wish)

@app.route('/test1')
def test1():
    test = "test"
    return make_response("test", test)


app.run(debug=True, port=8080)
