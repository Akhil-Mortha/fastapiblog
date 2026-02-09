# FastAPI Blog API

A backend REST API built using FastAPI for creating and managing blogs and users.

## Features
- CRUD Blog APIs
- User authentication
- Password hashing
- JWT authentication
- SQLite database

## Tech Stack
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

## Run Locally

```bash
git clone https://github.com/yourusername/blog.git
cd blog
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
                               