from http import HTTPStatus

import json

from flask import Flask, request, Response
from src.functions.dummy_function import square_number

app = Flask(__name__)


@app.route('/ping')
def ping():
    return 'pong'


@app.route('/square', methods=['POST'])
def square():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        input_json = request.json

        input_number = input_json['input']

        try:
            result_number = square_number(input_number)

            result = Response(
                response=json.dumps({'result': result_number}),
                status=HTTPStatus.OK,
                mimetype='application/json'
            )

        except TypeError:
            result = Response(
                response='Input error - input should be numerical',
                status=HTTPStatus.UNPROCESSABLE_ENTITY,
                mimetype='application/json'
            )

    else:
        result = Response(
            response='Content-Type not supported!',
            status=HTTPStatus.UNPROCESSABLE_ENTITY,
            mimetype='application/json'
        )

    return result
