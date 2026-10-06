# Lab 5 - Postman and APIs

This project is for Lab 5 of EECE435L.

The goal of the lab is to build a Flask REST API connected to an SQLite database and test the API using Postman.

## Project Features

The API supports the following operations:

- Add a user
- Get all users
- Get a user by ID
- Update a user
- Delete a user

## Project Files

- `app.py` - Flask application and API routes
- `database.py` - SQLite database functions
- `database.db` - SQLite database
- `Flask user app.postman_collection.json` - Postman collection used to test the API
- `screenshots/` - Screenshots of the API requests and responses

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/users` | Get all users |
| GET | `/api/users/<user_id>` | Get one user by ID |
| POST | `/api/users/add` | Add a new user |
| PUT | `/api/users/update` | Update an existing user |
| DELETE | `/api/users/delete/<user_id>` | Delete a user |

## Running the Application

Create and activate a virtual environment, then install the required packages:

```bash
pip install flask flask-cors db-sqlite3