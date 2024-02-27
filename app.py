#!/usr/bin/env python

"""
QR code generation API. Provides endpoints for generating QR codes and saving data to the database.

The '/' endpoint returns a simple GET response.

The '/qr_code' endpoint takes a JSON payload and generates a QR code image using the helper module. Returns filename of generated image.

The '/save_to_db' endpoint takes a JSON payload and saves it to the database after generating a QR code. Returns QR code filename.
"""

"""Contains the flask app"""

from flask import Flask, request, jsonify
from models.helper import User, generate_qr_code
from upload import upload, get_qrcode

app = Flask(__name__)

@app.route("/", methods=['GET'], strict_slashes=False)
def home():
    """home route"""
    return "hello world"

@app.route("/create_qr_code", methods=["POST"], strict_slashes=False)
def submit():
    """Expects a JOSN data, creates the QR code, saves it in the database"""
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    try:
        qr_code_path, employee_information = generate_qr_code(**data)
        qr_id = upload(qr_code_path, employee_information)
        return jsonify({
            "message": "QR code generated successfully",
            "user": employee_information.dict(),
            "qr_code_path": qr_code_path,
            "qr_id": qr_id
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/fetch_qr_code/<database_id>", methods=["GET"], strict_slashes=False)
def get_code(database_id):
    """fetches the qr_code from the database"""
    # TODO create a function that fetch a particular qrcode using the id 
    try:
        qr_code_path = get_qrcode(database_id)
        print(qr_code_path)
        return jsonify({
                "message": "QR code retrieved successfully",
                "qr_code_path": qr_code_path,
            })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3001, debug=True)

