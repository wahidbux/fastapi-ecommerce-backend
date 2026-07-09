# FastAPI E-Commerce Backend

A backend project demonstrating how to build a full e-commerce REST API with FastAPI and PostgreSQL. This repository covers core backend concepts including authentication, role-based authorization, relational data modeling, and order processing logic.

## Features

* User Registration & Login
* Password hashing with bcrypt
* JWT token-based authentication
* Role-based access control (user vs. admin)
* Product catalog with full CRUD (admin-only write access)
* Shopping cart management
* Cart-to-checkout order flow with stock validation
* Order history per user
* Request validation with Pydantic
* PostgreSQL database integration
* Interactive API documentation (Swagger UI & ReDoc)

## Tech Stack

* Python 3
* FastAPI
* SQLAlchemy
* PostgreSQL
* bcrypt
* python-jose
* Pydantic
* Uvicorn
* python-dotenv

## Installation

Clone the repository and install the dependencies:

```
git clone https://github.com/YOUR_USERNAME/fastapi-ecommerce-backend.git
cd fastapi-ecommerce-backend
pip install -r requirements.txt
```

Set up environment variables:

```
DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/ecommerce_db
SECRET_KEY=your-secret-key-here
```

Generate a secret key: `openssl rand -hex 32`

Run the application:

```
uvicorn app.main:app --reload
```

Open your browser:

* API: http://127.0.0.1:8000
* Swagger UI: http://127.0.0.1:8000/docs
* ReDoc: http://127.0.0.1:8000/redoc

## Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/users/register` | Create a new account |
| POST | `/users/login` | Login and receive a JWT token |
| GET | `/users/me` | Get current user profile |
| GET | `/products/` | List all products |
| GET | `/products/{id}` | Get a single product |
| POST | `/products/` | Create a product (admin only) |
| PUT | `/products/{id}` | Update a product (admin only) |
| DELETE | `/products/{id}` | Delete a product (admin only) |
| GET | `/cart/` | View current user's cart |
| POST | `/cart/add` | Add an item to the cart |
| DELETE | `/cart/{item_id}` | Remove an item from the cart |
| POST | `/orders/checkout` | Convert cart into an order |
| GET | `/orders/` | List current user's orders |
| GET | `/orders/{id}` | Get details of a specific order |

## Topics Covered

* FastAPI project structure
* Password hashing with bcrypt
* JWT creation & verification
* Role-based access control & Dependency Injection
* SQLAlchemy ORM & PostgreSQL integration
* Relational data modeling (one-to-many, foreign keys)
* Cart and order business logic
* Request validation with Pydantic
* Exception handling

## Purpose

This project was built to strengthen my backend development skills and gain hands-on experience designing a realistic, multi-resource API — covering authentication, authorization, relational database design, and transactional business logic with FastAPI.