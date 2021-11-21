import json

from flask import Flask, jsonify
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World 2 !</h1>'


@app.route('/series/', methods=['POST'])
def new_series():
    series = request.json
    return '<h1>Waiting for results</h1>' +  json.dumps(series)


if __name__ == '__main__':
    app.run(debug=True)
