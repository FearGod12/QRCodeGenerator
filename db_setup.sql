CREATE DATABASE betakopa_qrcodes;
\connect betakopa_qrcodes
CREATE TABLE IF NOT EXISTS qrcode (
    id SERIAL PRIMARY KEY,
    employee_name VARCHAR(255),
    personal_website VARCHAR(255),
    phone_number VARCHAR(20),
    email_address VARCHAR(255),
    qr_image BYTEA
);
