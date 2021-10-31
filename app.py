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
def hello():
    bye = "bye"
    return make_response("bye", bye)

@app.route('/test1')
def test1():
    test = "test"
    return make_response("test", test)

@app.route('/test2')
def test2():
    test2 = "test2"
    return make_response("test2", test2)

@app.route('/test3')
def test3():
    test3 = "test3"
    return make_response("test3", test3)

@app.route('/test4')
def test4():
    test4 = "test4"
    return make_response("test4", test4)

@app.route('/test5')
def test5():
    test5 = "test5"
    return make_response("test5", test5)

@app.route('/test6')
def test6():
    test6 = "test6"
    return make_response("test6", test6)

@app.route('/test7')
def test7():
    test7 = "test7"
    return make_response("test7", test7)

@app.route('/test8')
def test8():
    test8 = "test8"
    return make_response("test8", test8)

@app.route('/test9')
def test9():
    test9 = "test9"
    return make_response("test9", test9)

@app.route('/test10')
def test10():
    test10 = "test10"
    return make_response("test10", test10)

@app.route('/test11')
def test11():
    test11 = "test11"
    return make_response("test11", test11)

@app.route('/test12')
def test12():
    test12 = "test12"
    return make_response("test12", test12)

@app.route('/test13')
def test13():
    test13 = "test13"
    return make_response("test13", test13)

app.run(debug=True, port=8080)
