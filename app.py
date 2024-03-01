#!/usr/bin/env python

"""
QR code generation API. Provides endpoints for generating QR codes and saving data to the database.

The '/' endpoint returns a simple GET response.

The '/qr_code' endpoint takes a JSON payload and generates a QR code image using the helper module. Returns filename of generated image.

The '/save_to_db' endpoint takes a JSON payload and saves it to the database after generating a QR code. Returns QR code filename.
"""

"""Contains the flask app"""
from io import BytesIO
from flask import Flask, request, jsonify, send_file, abort

from models.helper import generate_qr_code
# import the upload function automatically executes the fucntion which sets up the database

from upload_and_fetch import upload, fetch_qr_code, fetch_user

app = Flask(__name__)

SAMPLE_DATA = {"qr_data":
               {"data_to_be_encoded": "https://google.com",
                "box_size": 10,
                "border": 4,
                "fill_color": "red",
                "back_color": "white"},
               "employee_information":
               {"employee_name": "TechJourneyMan",
                "phone_number" : 1234567,
                "email_address": "onyenikechukwudi@gmail.com"
                }}


@app.route("/", methods=['GET'], strict_slashes=False)
def home():
    return "Hello, world!"

@app.route("/create_qr_code", methods=["POST"], strict_slashes=False)
def submit():
    """Expects a json data, creates the qr_code, save it in the db"""
    try:
        data = request.get_json(silent=True)
        img_bytes, employee_information = generate_qr_code(data)
        result = upload(img_bytes, employee_information)
        print(result)
        return jsonify({"Success": "QR code generated and saved successfully", "id": f"{result}"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/fetch_qr_code/<database_id>", methods=["GET"], strict_slashes=False)
def get_code(database_id):
    """fetches the qr_code from the database"""
    try:
        qr_code = fetch_qr_code(database_id)
        if qr_code is None:
            abort(404, "QR code not found")
        img_buffer = BytesIO(qr_code)
        return send_file(img_buffer, mimetype='image/png', as_attachment=True, download_name='qrcode.png')

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route("/fetch_user/<database_id>", methods=["GET"], strict_slashes=False)
def get_user(database_id):
    """fetches a user data as json"""
    result = fetch_user(database_id)
    if result:
        return jsonify(result), 200
    return abort(404, "User not found")


@app.route("/fetch_all_users", methods=["GET"], strict_slashes=False)
def get_all_users():
    """fetches all users in the database"""
    return jsonify({"error": "Not yet implemented"}), 501


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3001, debug=True)
