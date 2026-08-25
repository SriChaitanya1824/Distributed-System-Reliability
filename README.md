# FastApiProj - Production-Ready Distributed System Reliability Boilerplate

A production-grade, asynchronous **FastAPI** web application engineered for high-availability, scalability, and distributed system reliability.

---

## 🌟 Key Features

- ⚡ **Asynchronous Core**: Fully async request handling with FastAPI and SQLAlchemy 2.0.
- 🗄️ **Database & ORM**: Asynchronous PostgreSQL (`asyncpg`) and SQLite fallback (`aiosqlite`) via SQLAlchemy 2.0 ORM.
- 🔐 **Authentication & Security**: JWT-based authentication with bcrypt password hashing and token expiration.
- 🛡️ **Role-Based Access Control (RBAC)**: Fine-grained user role permissions (Admin, Moderator, User).
- ⏳ **Rate Limiting**: Distributed rate limiting using `SlowAPI` to prevent denial-of-service and abuse.
- 📦 **Redis & Background Jobs**: Redis integration with `ARQ` for distributed background task execution.
- 📊 **Observability & Metrics**: Built-in Prometheus metrics (`/metrics`) alongside Kubernetes health, liveness (`/live`), and readiness (`/ready`) endpoints.
- 🧪 **Testing Suite**: Comprehensive pytest test suite with isolated database configurations.
- 🐳 **Containerization**: Complete Docker and `docker-compose` configuration for effortless container deployment.

---

## 📁 Repository Structure

```text
FastApiProj/
├── alembic/              # Database migration scripts and configurations
├── app/                  # Main application package
│   ├── api/              # API route definitions and dependencies
│   │   ├── deps/         # Security and pagination dependencies
│   │   └── v1/           # API v1 routers (auth, users, items)
│   ├── core/             # Application configuration, limiter, and Redis client
│   ├── db/               # Async database connection and session management
│   ├── middleware/       # Structured JSON logging and CORS middlewares
│   ├── models/           # SQLAlchemy models and audit mixins
│   ├── repositories/     # Generic repository layer for DB operations
│   └── schemas/          # Pydantic V2 data validation schemas
├── tests/                # Automated pytest test cases
├── alembic.ini           # Alembic configuration file
├── Dockerfile            # Production Docker image build file
├── docker-compose.yml    # Docker Compose multi-container orchestrator
└── pyproject.toml        # Project dependencies and tool configurations
```

---

## 🚀 Quick Start Guide

### 1. Prerequisites

- Python 3.9+ installed
- Redis (optional for caching / background workers)
- PostgreSQL or SQLite

### 2. Environment Setup

Clone the repository and set up a virtual environment:

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

Create a `.env` file in the root directory (optional, sensible defaults provided):

```env
ENVIRONMENT=development
DATABASE_URL=sqlite+aiosqlite:///./test.db
REDIS_URL=redis://localhost:6379/0
SECRET_KEY=dev-secret-key-change-in-production
```

### 3. Running the Server

Start the FastAPI application using Uvicorn:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Once running, access:
- **Interactive API Docs (Swagger UI)**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc Documentation**: [http://localhost:8000/redoc](http://localhost:8000/redoc)
- **Health Probe**: [http://localhost:8000/health](http://localhost:8000/health)

---

## 🧪 Running Tests

Execute the automated test suite:

```bash
ENVIRONMENT=testing pytest
```

---

## 🐳 Running with Docker

Build and start all services using Docker Compose:

```bash
docker-compose up --build
```

---

## 📄 License

This project is licensed under the MIT License.
