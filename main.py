#!/usr/bin/env python
from flask import Flask, render_template

app = Flask(__name__, static_url_path='')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/healthz')
def health_check():
    return {'status': True}
