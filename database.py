import psycopg2

params = {
    "host": "localhost",
    "port": 5432,
    "database": "BetaKopa_qrcodes",
    "user": "postgres",
    "password": "Chuks123."
}

def connect():
    """
    Connects to a PostgreSQL database using the provided configuration.
    Prints a message indicating whether the connection was successful.
    Returns the database connection object on success.
    """
    try:
        # connecting to the PostgreSQL server
        conn = psycopg2.connect(**params)
        print('Connected to the PostgreSQL server.')
        
        # Create a cursor object
        cursor = conn.cursor()
        
        # Execute the SQL query to create the table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS qrcode(
                id SERIAL PRIMARY KEY,
                employee_name VARCHAR,
                personal_website VARCHAR,
                phone_number INT,
                email_address VARCHAR,
                qr_image BYTEA
            )
        """)
        
        # Commit the transaction
        conn.commit()
        
        # Close the cursor
        cursor.close()
        
        return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


if __name__ == "__main__":
    connect()