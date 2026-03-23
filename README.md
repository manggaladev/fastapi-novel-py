# 📚 FastAPI Novel API

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success?style=flat-square)](https://github.com/manggaladev/fastapi-novel-py)

A FastAPI project for managing novels and chapters. This is a learning project to rebuild features from an Express/TypeScript novel-api.

## ✨ Features

- **🔐 User Authentication** - JWT-based authentication with role-based access control
- **📚 Novel Management** - CRUD operations for novels with author ownership
- **📖 Chapter Management** - CRUD operations for chapters with unique constraints
- **📄 Pagination** - All list endpoints support pagination
- **⚠️ Error Handling** - Consistent JSON error responses
- **📖 API Documentation** - Auto-generated OpenAPI docs with Swagger UI and ReDoc

## 🛠️ Tech Stack

- **Framework**: FastAPI
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Migrations**: Alembic
- **Authentication**: JWT (python-jose)
- **Password Hashing**: bcrypt (passlib)

## 📦 Installation

### Local Development

```bash
# Clone the repository
git clone https://github.com/manggaladev/fastapi-novel-py.git
cd fastapi-novel-py

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Copy environment file
cp .env.example .env

# Run database migrations
alembic upgrade head

# Start the server
uvicorn app.main:app --reload
```

### Docker

```bash
# Build and run
docker-compose up -d

# Run migrations
docker-compose exec app alembic upgrade head
```

## 🚀 Usage

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/register` | Register new user |
| POST | `/auth/login` | Login user |
| GET | `/novels` | List all novels |
| POST | `/novels` | Create novel (author) |
| GET | `/novels/{id}` | Get novel details |
| PUT | `/novels/{id}` | Update novel (owner) |
| DELETE | `/novels/{id}` | Delete novel (owner) |
| GET | `/novels/{id}/chapters` | List chapters |
| POST | `/novels/{id}/chapters` | Create chapter (owner) |

### API Documentation

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 📁 Project Structure

```
fastapi-novel-py/
├── app/
│   ├── __init__.py
│   ├── main.py           # FastAPI app
│   ├── api/              # API routes
│   ├── core/             # Config, security
│   ├── models/           # SQLAlchemy models
│   ├── schemas/          # Pydantic schemas
│   └── services/         # Business logic
├── alembic/              # Migrations
├── alembic.ini
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

## 📄 License

[MIT License](LICENSE)

