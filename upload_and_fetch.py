#!/usr/bin/env python

from database import connect
import psycopg2
from io import BytesIO

# Establish connection to the database
try:
    connection = connect()
except Exception as e:
    print("Error connecting to the database:", e)
    exit()

cur = connection.cursor()

def upload(img_bytes, employee_information):
    '''
    this function accepts data in binary data of the QR code image and the employee information
    '''
    try: 
        employee_name = employee_information.employee_name
        personal_website = employee_information.personal_website
        phone_number = employee_information.phone_number
        email_address = employee_information.email_address
        
        # Execute the query to insert data into the qrcode table
        query = """
            INSERT INTO qrcode (employee_name, personal_website, phone_number, email_address, qr_image)
            VALUES (%s, %s, %s, %s, %s)
        """
        cur.execute(query, (employee_name, personal_website, phone_number, email_address, img_bytes))
        # Get the ID of the last inserted row using currval function
        cur.execute("SELECT currval(pg_get_serial_sequence('qrcode', 'id'))")
        inserted_id = cur.fetchone()[0]
        print("Inserted successfully")
        
        # Commit the transaction
        connection.commit()
        return inserted_id
    except (Exception, psycopg2.Error) as error:
        print("Error inserting QR code into database:", error)
        connection.rollback()

def fetch_qr_code(database_id: int):
    """fetches a qr_code from db"""
    query = f"""SELECT qr_image FROM qrcode WHERE id={database_id}"""
    cur.execute(query)    
    result = cur.fetchone()
    if result:
        return result[0].tobytes()
    return None

def fetch_user(database_id):
    """fetches info about the user with the id"""
    query = f"""SELECT employee_name, personal_website, phone_number, email_address FROM qrcode WHERE id={database_id}"""
    cur.execute(query)
    result = cur.fetchone()
    if result:
        columns = [column[0] for column in cur.description]
        user_data = dict(zip(columns, result))
        return user_data
    return result
