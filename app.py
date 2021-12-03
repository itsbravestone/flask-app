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

@app.route('/bye')
def bye():
    bye = "bye"
    return make_response("bye", bye)

@app.route('/test1')
def test1():
    test = "test"
    return make_response("test", test)

@app.route('/test2')
def test2():
    test = "test"
    return make_response("test", test)

@app.route('/test3')
def test3():
    test = "test"
    return make_response("test", test)

@app.route('/test4')
def test4():
    test = "test"
    return make_response("test", test)

@app.route('/test5')
def test5():
    test = "test"
    return make_response("test", test)

@app.route('/test6')
def test6():
    test = "test"
    return make_response("test", test)

@app.route('/test7')
def test7():
    test = "test"
    return make_response("test", test)

@app.route('/test8')
def test8():
    test = "test"
    return make_response("test", test)

@app.route('/test9')
def test9():
    test = "test"
    return make_response("test", test)

app.run(debug=True, port=8080)
