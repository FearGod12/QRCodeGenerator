#!/usr/bin/env python

"""Contains the flask app"""
from flask import Flask, request
from models import helper 

app = Flask(__name__)


@app.route("/")
def index():
    if request.method == "GET":
        print("Get")
        return ({"message": "GET"})

@app.route("/qr_code", methods=["POST"])
def qr_code():
   data = request.get_json()
   helper.generate_qr_code(**data)
       