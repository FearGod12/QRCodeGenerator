CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL
);

CREATE TABLE QRCode (
    qrcode_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES Users(user_id),
    data TEXT NOT NULL,
    metadata JSONB,
    generated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    qr_code_img BYTEA
);

/*
Database Schema Documentation

Users Table:

The Users table stores information about users who interact with the QR code generator application.

Columns:
- user_id: A unique identifier for each user. Automatically generated using the SERIAL data type.
- username: The username of the user. It is a VARCHAR field with a maximum length of 50 characters.
- email: The email address of the user. It is a VARCHAR field with a maximum length of 100 characters.

QRCode Table:

The QRCode table stores information about generated QR codes.
Columns:
- qrcode_id: A unique identifier for each QR code. Automatically generated using the SERIAL data type.
- user_id: The foreign key referencing the user_id column in the Users table, indicating the user who generated the QR code.
- data: The data encoded in the QR code. It is stored as TEXT.
- metadata: Additional metadata associated with the QR code, stored as JSONB (binary JSON).
- generated_at: The timestamp indicating when the QR code was generated. Defaults to the current timestamp when a new record is inserted into the table.
- qr_code_image: A column for the qrcode image
*/
