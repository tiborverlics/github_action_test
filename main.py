from flask import Flask, request
from src.functions.dummy_function import square_number

app = Flask(__name__)


@app.route('/ping')
def ping():
    return 'pong'


@app.route('/square', methods=['POST'])
def square():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json = request.json

        input_number = json['input']

        return {'result': square_number(input_number)}
    else:
        return 'Content-Type not supported!'
