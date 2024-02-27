import os
import uuid
import qrcode
from pydantic import BaseModel, ValidationError, EmailStr, HttpUrl
from io import BytesIO

# """Generates a UUID for an employee and creates a QR code encoding their name, 
# employee ID, and generated UUID.

# The generate_uuid function generates a random UUID for the given employee name and ID.
# The generate_qr_code function takes a dict with employee name, ID, and UUID, and creates a QR code 
# encoding that data. The QR code is saved to a PNG file named after the employee. The filename is returned.
# """


class User(BaseModel):
    name: str
    employee_id: str = None
    personal_website : str = None
    phone_number : str
    email_address: str = None
    

#TODO add encryption for sensitive data
def generate_uuid() -> str:
    return str(uuid.uuid4())


def generate_qr_code(**data:dict) -> str:
    "This function creates and save our qrcode information"
    #TODO check what data type is data
    try:
        employee_information = User(**data)
        employee_information.employee_id = generate_uuid()
        
        qr_data = employee_information.json()
        
        # Create a folder to save the QR codes generated
        folder_path = "qr_codes"
        os.makedirs(folder_path, exist_ok=True)
        
        # Make the file name unique in the format `name_uuid`
        filename = f"{employee_information.name}_{employee_information.employee_id}.png"
        filepath = os.path.join(folder_path, filename)
        
        img = qrcode.make(qr_data)
        img.save(filepath)
        print("Success, the file name is: " + filename)
        return filepath, employee_information
    
    except ValidationError as e:
        print("Validation Error occured: " + str(e))
        raise
        

# info = {
#     "user_name": "Fred",
#     "personal_website" : 1,
#     "phone_number" : "07042802954",
#     "email_address": "jlsdjnpsoiq",
#     "employee_id": "123444"
    
# }

# print(generate_qr_code(**info))