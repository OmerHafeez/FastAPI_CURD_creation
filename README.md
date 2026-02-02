# FastAPI CRUD Application

A simple RESTful API built with FastAPI for managing items with full CRUD (Create, Read, Update, Delete) operations.

## Features

- ✅ Create, read, update, and delete items
- ✅ SQLite database with SQLAlchemy ORM
- ✅ Fast and async API endpoints
- ✅ Auto-generated API documentation

## Technologies

- **FastAPI** - Modern web framework for building APIs
- **SQLAlchemy** - SQL toolkit and ORM
- **Uvicorn** - ASGI web server
- **SQLite** - Lightweight database

## Installation

1. Clone the repository
```bash
git clone <your-repo-url>
cd FastApiCRUD
```

2. Create and activate virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies
```bash
pip install fastapi uvicorn sqlalchemy
```

## Running the Application

```bash
python -m uvicorn main:app --reload
```

Or use the included script:
```bash
./run.sh
```

The API will be available at `http://127.0.0.1:8000`

## API Endpoints

________________________________________________
| Method | Endpoint      | Description         |
|--------|---------------|---------------------|
| GET    | `/items`      | Get all items       |
| GET    | `/items/{id}` | Get a specific item |
| POST   | `/items`      | Create a new item   |
| PUT    | `/items/{id}` | Update an item      |
| DELETE | `/items/{id}` | Delete an item      |
------------------------------------------------

## API Documentation

Once running, visit:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Project Structure

```
FastApiCRUD/
├── main.py          # API routes and app initialization
├── database.py      # Database configuration
├── model.py         # SQLAlchemy models
├── schemas.py       # Pydantic schemas
├── crud.py          # CRUD operations
├── Auth.py          # Authentication (if needed)
└── run.sh           # Quick start script
```


