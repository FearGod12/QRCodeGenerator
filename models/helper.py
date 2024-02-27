#!/usr/bin/env python
import uuid0
import qrcode
from pydantic import BaseModel, ValidationError
from io import BytesIO

# """Generates a UUID for an employee and creates a QR code encoding their name, 
# employee ID, and generated UUID.

# The generate_uuid function generates a random UUID for the given employee name and ID.
# The generate_qr_code function takes a dict with employee name, ID, and UUID, and creates a QR code 
# encoding that data. The QR code is saved to a PNG file named after the employee. The filename is returned.
# """


class User(BaseModel):
    employee_name: str
    personal_website : str = None
    phone_number : int
    email_address: str
    employee_id: str = None
    employee_uuid: str = None
    

#TODO add encryption for sensitive data
def generate_uuid(input_data:dict) -> str:
    user_details = input_data
    uuid = str(uuid0.generate())
    return uuid

def generate_qr_code(data: dict) -> bytes:
    """
    This function generates a QR code image based on the provided data and customization options.
    :param data: A dictionary containing the data to be encoded and customization options.
    :return: Bytes data of the generated QR code image.
    """
    try:
        employee_information = User(**data["employee_information"])
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level: L, M, Q, H
            box_size=data["qr_data"].get('box_size', 10),  # Size of each box in the QR code
            border=data["qr_data"].get('border', 4),  # Size of the border around the QR code
        )
        qr.add_data(data["qr_data"]["data_to_be_encoded"])
        qr.make(fit=True)

        img_buffer = BytesIO()

        img = qr.make_image(fill_color=data["qr_data"].get('fill_color', 'black'), back_color=data["qr_data"].get('back_color', 'white'))
        img.save("qr_code.png")
        img.save(img_buffer, 'PNG')
        img_buffer.seek(0)

        img_bytes = img_buffer.getvalue()
        return img_bytes, employee_information
    except ValidationError as e:
        raise ValueError(f"Validation error: {e}")
