# Novel Management API

A FastAPI project for managing novels and chapters. This is a learning project to rebuild features from an Express/TypeScript novel-api.

## Features

- **User Authentication**: JWT-based authentication with role-based access control
- **Novel Management**: CRUD operations for novels with author ownership
- **Chapter Management**: CRUD operations for chapters with unique constraints
- **Pagination**: All list endpoints support pagination
- **Error Handling**: Consistent JSON error responses
- **API Documentation**: Auto-generated OpenAPI docs with Swagger UI and ReDoc

## Tech Stack

- **Framework**: FastAPI
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Migrations**: Alembic
- **Authentication**: JWT (python-jose)
- **Password Hashing**: bcrypt (passlib)
- **Validation**: Pydantic

## Installation

### Prerequisites

- Python 3.10+
- PostgreSQL

### Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd fastapi-novel-py
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your database credentials
   ```

5. Create the PostgreSQL database:
   ```sql
   CREATE DATABASE novel_db;
   ```

6. Run migrations:
   ```bash
   alembic revision --autogenerate -m "Initial migration"
   alembic upgrade head
   ```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | PostgreSQL connection URL | Required |
| `JWT_SECRET` | Secret key for JWT tokens | Required |
| `JWT_ALGORITHM` | Algorithm for JWT | `HS256` |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token expiration time | `30` |

## Running the Server

### Development

```bash
uvicorn app.main:app --reload
```

### Production

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## API Endpoints

### Authentication

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| POST | `/auth/register` | Register a new user | No |
| POST | `/auth/login` | Login and get token | No |
| GET | `/auth/me` | Get current user info | Yes |

### Novels

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| GET | `/novels` | List all novels (paginated) | No |
| GET | `/novels/{id}` | Get a single novel | No |
| POST | `/novels` | Create a novel | Yes |
| PUT | `/novels/{id}` | Update a novel | Owner/Admin |
| DELETE | `/novels/{id}` | Delete a novel | Owner/Admin |

### Chapters

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| GET | `/novels/{novel_id}/chapters` | List chapters for a novel | No |
| GET | `/chapters/{id}` | Get a single chapter | No |
| POST | `/novels/{novel_id}/chapters` | Create a chapter | Owner/Admin |
| PUT | `/chapters/{id}` | Update a chapter | Owner/Admin |
| DELETE | `/chapters/{id}` | Delete a chapter | Owner/Admin |

## Pagination

All list endpoints return paginated results:

```json
{
  "items": [...],
  "total": 100,
  "page": 1,
  "limit": 10,
  "total_pages": 10
}
```

Query parameters:
- `page`: Page number (default: 1)
- `limit`: Items per page (default: 10, max: 100)

## User Roles

| Role | Permissions |
|------|-------------|
| `user` | Can create novels and manage their own content |
| `author` | Can create novels and manage their own content |
| `admin` | Full access to all resources |

## Project Structure

```
fastapi-novel-py/
├── app/
│   ├── api/
│   │   ├── dependencies/
│   │   │   └── auth.py          # Auth dependencies
│   │   ├── routes/
│   │   │   ├── auth.py          # Auth routes
│   │   │   ├── novels.py        # Novel routes
│   │   │   └── chapters.py      # Chapter routes
│   │   └── __init__.py
│   ├── core/
│   │   ├── config.py            # Settings
│   │   ├── database.py          # Database setup
│   │   ├── security.py          # Security utilities
│   │   └── __init__.py
│   ├── models/
│   │   ├── user.py              # User model
│   │   ├── novel.py             # Novel model
│   │   ├── chapter.py           # Chapter model
│   │   └── __init__.py
│   ├── schemas/
│   │   ├── user.py              # User schemas
│   │   ├── novel.py             # Novel schemas
│   │   ├── chapter.py           # Chapter schemas
│   │   └── __init__.py
│   ├── services/
│   │   ├── auth.py              # Auth service
│   │   ├── novel.py             # Novel service
│   │   ├── chapter.py           # Chapter service
│   │   └── __init__.py
│   └── main.py                  # FastAPI app
├── alembic/                     # Migrations
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## API Documentation

Once the server is running, access the documentation at:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Migrations

### Create a new migration

```bash
alembic revision --autogenerate -m "Description of changes"
```

### Apply migrations

```bash
alembic upgrade head
```

### Rollback migration

```bash
alembic downgrade -1
```

## License

MIT
