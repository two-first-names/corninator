#!/usr/bin/env python
from flask import Flask, render_template, request, jsonify

from crossing import cost_for_crossing, result
from exceptions import InvalidUsage

app = Flask(__name__, static_url_path='')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/healthz')
def health_check():
    return {'status': True}


@app.route('/crossing')
def crossing():
    bags = int(request.args.get('bags', 0))
    geese = int(request.args.get('geese', 0))
    return {
        'cost': cost_for_crossing(bags),
        'message': result(bags, geese)
    }


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


if __name__ == '__main__':
    app.run()