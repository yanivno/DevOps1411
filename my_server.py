import requests
from flask import Flask, request

app = Flask("something")


@app.route('/whatismyname', methods=['GET', 'POST', 'DELETE'])
def hello():
    my_score = 1
    if request.method == 'GET':
        return '<h1><div id="moshe">mazda, citroen, chevrolet</div></h1>'
    elif request.method == 'POST':
        return "saved new car"
    # return "<h1>" + str(my_score) + "</h1>"


@app.route('/cars', methods=['GET', 'POST', 'DELETE'])
def get_cars():
    if request.method == 'GET':
        my_file = open("cars.txt", "r")
        my_file = str(my_file.readlines())
        return my_file


@app.route('/')
def my_func():
    return "hello and welcome to the world of games"


app.run(host="0.0.0.0", port=5001, debug=True)