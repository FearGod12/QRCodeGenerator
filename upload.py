#!/usr/bin/env python

from database import connect
import psycopg2
from models.helper import User



def upload(filepath, employee_information):
    '''
    This function uploads and saves the generated accepts data in binary data of the QR code image
    '''
    connection = connect()
    try:
        with connection.cursor() as cursor:
        
            with open(filepath, 'rb') as qr_file:
                qr_image_data = qr_file.read()
                
                query = """
                INSERT INTO qrcode (employee_name, personal_website, phone_number, email_address, qr_image)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING id
                """
                
                cursor.execute(query, (
                    employee_information.name,
                    employee_information.personal_website,
                    employee_information.phone_number,
                    employee_information.email_address,
                    qr_image_data
                ))
                qr_id = cursor.fetchone()[0]
                                
                # Persist the data on the database
                connection.commit()

                return qr_id

    except (Exception, psycopg2.Error) as error:
        print("Error inserting data into database:", error)
       
        
    finally:
        # Close the connection
        if connection is not None:
            connection.close()

def get_qrcode(id: str):
    '''
    This function retrieves the generated QR code image
    '''
    connection = connect()
    try:
        with connection.cursor() as cursor:
            query = """
            SELECT * IN qrcode
            WHERE id = (%s)
            """
            
            qr_code = cursor.execute(query, id)
            
            # qr_code = cursor.fetchone()[0]
                            
            # Persist the data on the database
            # connection.commit()

            return qr_code

    except (Exception, psycopg2.Error) as error:
        print("Error fetching data from the database:", error)
        raise
       
        
    finally:
        # Close the connection
        if connection is not None:
            connection.close()
