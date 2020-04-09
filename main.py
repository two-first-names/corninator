#!/usr/bin/env python
from flask import Flask, render_template, request

from crossing import cost_for_crossing

app = Flask(__name__, static_url_path='')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/healthz')
def health_check():
    return {'status': True}


@app.route('/crossing')
def crossing():
    bags = int(request.args['bags'])
    return {
        'cost': cost_for_crossing(bags)
    }
