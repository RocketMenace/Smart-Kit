# Cadastral Records Internship Application 🏛️



> Secure API for cadastral number processing that validates records through third-party verification before PostgreSQL storage, with JWT authentication and Redis token blacklisting.

## Features 🔍

- **Secure Authentication** using JWT with token blacklisting via Redis
- **Cadastral Number Processing** with third-party verification
- **RESTful API** built with FastAPI (OpenAPI documentation included)
- **Database Migrations** using Alembic
- **Comprehensive Testing** with Pytest
- **Containerized Deployment** with Docker & Docker-compose
- **HTTP External Requests** via httpx client

## Installation & Launch 🚀
```bash
# Clone the repository
git clone https://github.com/RocketMenace/Smart-Kit.git


# Build and launch containers
docker-compose up --build

Environment Configuration ⚙️

Create .env file with these variables:

# Environment state (test/dev)
ENV_STATE=

# Development DB
DEV_POSTGRES_USER=
DEV_POSTGRES_PASSWORD=
DEV_POSTGRES_SERVER=
DEV_POSTGRES_PORT=
DEV_POSTGRES_DB=

# Production DB
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_SERVER=
POSTGRES_PORT=
POSTGRES_DB=

# Redis
DEV_REDIS_SERVER=
DEV_REDIS_PORT=

# API
DEV_API_KEY=

# Test environment
TEST_REDIS_SERVER=
TEST_REDIS_PORT=
TEST_POSTGRES_USER=
TEST_POSTGRES_PASSWORD=
TEST_POSTGRES_SERVER=
TEST_POSTGRES_PORT=
TEST_POSTGRES_DB=
TEST_API_KEY=

## API Endpoints 📡

**Interactive Documentation:** [Swagger UI](http://127.0.0.1:8000/api/docs) | [ReDoc](http://127.0.0.1:8000/api/redoc)

| Endpoint            | Method | Description                        |
|---------------------|--------|------------------------------------|
| `/history`          | GET    | Fetch all cadastral records        |
| `/query`            | POST   | Register new cadastral number      |
| `/ping`             | GET    | Check third-party server status    |
| `/users/register`   | POST   | Register new user                  |
| `/users/login`      | POST   | User login                         |
| `/users/logout`     | POST   | User logout                        |
| `/users/refresh`    | POST   | Refresh JWT tokens                 |
| `/api/admin`        |        | Amin panel                         |     

