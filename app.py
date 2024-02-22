#!/usr/bin/env python

"""Contains the flask app"""

from flask import Flask

app = Flask(__name__)

@app.route('/generate_url_qr')
def generate_url_qr():
    # Logic for generating QR code for URL
    return 'QR code for URL generated'
