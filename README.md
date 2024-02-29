# QR Code Generator App

## Setup

### Create a virtual environment

```
python -m venv venv
source venv/bin/activate
```

### Install dependencies

```
pip install -r requirements.txt
```

### Create PostgreSQL database

```sql
CREATE DATABASE qrcode_db;
```

### Run database setup script

```
python database.py
```

This will create the necessary tables.

### Start the app

```
python app.py
```

The app will be served at http://localhost:3001

## Usage

The app contains the following endpoints:

### POST /create_qr_code

Generates and saves a QR code to the database.

**Request body:**

```json
{
  "qr_data": {
    "data_to_be_encoded": "https://www.example.com",
    "box_size": 10,
    "border": 4,
    "fill_color": "black",
    "back_color": "white"
  },

  "employee_information": {
    "employee_name": "John Doe",
    "phone_number": 123456789,
    "email_address": "john@example.com"
  }
}
```

**Response:**

```
Status Code: 201

{
  "Success": "QR code generated and saved successfully",
  "id": 1
}
```

### GET /get_qr_code/:id

Retrieves a QR code by id.

**Response:**

```
Status Code: 200

{image/png data}
```

### GET /fetch_user/:id

Retrieves user data associated with a QR code id.

**Response:**

```
Status Code: 200

{
  "employee_name": "John Doe",
  "phone_number": 123456789,
  "email_address": "john@example.com"
}
```

# API Documentation

## Endpoints

### `GET /fetch_qr_code/<:id>`

Fetches a QR code image from the database.

**Response:**

QR code image with content-type "image/png"

### `GET /fetch_user/<:id>`

Fetches user information associated with a QR code id.

**Request:**

QR code id

**Response:**

```json
{
  "id": 1,
  "employee_name": "John Doe",
  "phone_number": 123456789,
  "email_address": "john@example.com"
}
```

Status Code: 200

### `GET /fetch_all_users`

Fetches information of all users.

**Response:**

```json
[
  {
    "id": 1,
    "employee_name": "John Doe",
    "phone_number": 123456789,
    "email_address": "john@example.com"
  },
  {
    "id": 2,
    "employee_name": "Jane Doe",
    "phone_number": 987654321,
    "email_address": "jane@example.com"
  }
]
```

\*\*
