<div align="center">

# ⚡ FastAPI Novel API

**A FastAPI implementation for managing novels and chapters - Learning project**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-336791?style=for-the-badge&logo=postgresql&logoColor=white)](https://postgresql.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

</div>

---

## 🎯 About

This is a **learning project** to rebuild features from an Express/TypeScript novel-api using **FastAPI** and **Python**. Great for comparing Node.js vs Python approaches!

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔐 **JWT Auth** | Access & refresh tokens |
| 👥 **RBAC** | Role-based access control |
| 📚 **Novels** | CRUD operations |
| 📖 **Chapters** | CRUD with pagination |
| 📄 **Pagination** | All list endpoints |
| 📖 **Auto Docs** | Swagger & ReDoc |

## 🚀 Quick Start

```bash
# Clone
cd fastapi-novel-py

# Create venv
python -m venv venv
source venv/bin/activate  # Linux/Mac

# Install
pip install -r requirements.txt

# Setup DB
alembic upgrade head

# Run
uvicorn app.main:app --reload
```

## 📖 API Documentation

| Docs | URL |
|------|-----|
| Swagger UI | `http://localhost:8000/docs` |
| ReDoc | `http://localhost:8000/redoc` |

## 📋 Endpoints

### Auth
```
POST /auth/register    # Register
POST /auth/login       # Login
POST /auth/refresh     # Refresh token
```

### Novels
```
GET  /novels           # List novels
POST /novels           # Create novel (author)
GET  /novels/{id}      # Get novel
PUT  /novels/{id}      # Update novel (owner)
DELETE /novels/{id}    # Delete novel (owner)
```

### Chapters
```
GET  /novels/{id}/chapters    # List chapters
POST /novels/{id}/chapters    # Create chapter
```

## 🏗️ Project Structure

```
fastapi-novel-py/
├── app/
│   ├── main.py          # FastAPI app
│   ├── api/
│   │   ├── routes/      # API endpoints
│   │   └── dependencies/# Auth deps
│   ├── core/            # Config, security
│   ├── models/          # SQLAlchemy models
│   ├── schemas/         # Pydantic schemas
│   └── services/        # Business logic
├── alembic/             # Migrations
├── requirements.txt
└── Dockerfile
```

## 🔧 Environment

```env
DATABASE_URL=postgresql://user:pass@localhost/db
JWT_SECRET=your-secret-key
JWT_REFRESH_SECRET=refresh-secret
```

## 🐳 Docker

```bash
docker-compose up -d
```

## 🆚 FastAPI vs Express

| Aspect | FastAPI | Express |
|--------|---------|---------|
| Typing | Pydantic | Zod/TypeScript |
| ORM | SQLAlchemy | Prisma |
| Docs | Auto | Manual (Swagger) |
| Async | Native | Promises |
| Speed | Very Fast | Fast |

## 🤝 Contributing

Contributions welcome!

## 📄 License

[MIT License](LICENSE)

---

<div align="center">

**[⬆ Back to Top](#-fastapi-novel-api)**


</div>
