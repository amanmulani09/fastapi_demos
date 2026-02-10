# FastAPI Demos

A comprehensive collection of FastAPI demonstrations showcasing different backend architectures, design patterns, and concepts. Each demo is a standalone project illustrating best practices for building production-ready APIs with FastAPI.

## 📚 Repository Purpose

This repository serves as a learning resource and reference implementation for:
- Modern Python backend development with FastAPI
- Common architectural patterns and best practices
- Integration with various databases and caching systems
- Authentication and authorization strategies
- Real-time communication patterns
- Performance optimization techniques

## 🚀 Projects

### 1. **Caching with Redis** (`caching_redis_fastapi/`)

Demonstrates implementing a caching layer using Redis to improve API performance.

**Key Features:**
- Redis integration with async support
- Cache-aside pattern implementation
- TTL (Time-To-Live) based cache expiration
- Pydantic model serialization for caching
- Application lifespan management for Redis connections

**Technologies:**
- FastAPI
- Redis (async)
- Pydantic

**Learn More:** [caching_redis_fastapi/README.md](caching_redis_fastapi/README.md)

---

### 2. **Authentication** (`fastapi_authentication/`)

Showcases various authentication mechanisms in FastAPI.

**Key Features:**
- JWT (JSON Web Token) authentication
- OAuth2 password flow
- Secure password hashing
- Protected route implementation
- Token-based authorization

**Technologies:**
- FastAPI
- Python-Jose (JWT)
- Passlib (password hashing)

---

### 3. **PostgreSQL Integration** (`fastapi_postgresql/`)

Full-stack CRUD application with PostgreSQL database integration.

**Key Features:**
- SQLAlchemy ORM integration
- Database session management
- Async database operations
- Repository pattern implementation
- Database migrations
- Relationship modeling (One-to-Many)

**Technologies:**
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic schemas

**Example Models:**
- Questions and Choices (polling system)

---

### 4. **Server-Sent Events** (`server_sent_events/`)

Real-time data streaming using Server-Sent Events (SSE).

**Key Features:**
- SSE implementation for real-time updates
- Unidirectional server-to-client streaming
- Event stream handling
- HTML client example

**Technologies:**
- FastAPI
- SSE (Server-Sent Events)
- HTML/JavaScript client

**Use Cases:**
- Live notifications
- Real-time dashboards
- Progress updates
- Live feeds

---

### 5. **Sync vs Async** (`sync_vs_async/`)

Performance comparison between synchronous and asynchronous endpoints.

**Key Features:**
- Side-by-side sync/async implementations
- Performance benchmarking
- Concurrency handling demonstrations
- Best practices for choosing sync vs async

**Technologies:**
- FastAPI
- asyncio

**Learn:**
- When to use async/await
- Performance implications
- Blocking vs non-blocking operations

---

## 🛠️ Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment tool (venv, virtualenv, or conda)
- Additional requirements per project (Redis, PostgreSQL, etc.)

### General Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd fastapi_demos
   ```

2. **Navigate to a specific project:**
   ```bash
   cd <project-name>
   ```

3. **Create and activate virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt  # If available
   # Or install FastAPI and uvicorn
   pip install fastapi uvicorn
   ```

5. **Run the application:**
   ```bash
   uvicorn app.main:app --reload
   # Or follow project-specific instructions
   ```

6. **Access the API:**
   - API: `http://localhost:8000`
   - Interactive docs: `http://localhost:8000/docs`
   - Alternative docs: `http://localhost:8000/redoc`

## 📖 Learning Path

**Recommended order for beginners:**

1. **Sync vs Async** - Understand FastAPI's async capabilities
2. **Authentication** - Learn security fundamentals
3. **PostgreSQL Integration** - Master database operations
4. **Caching with Redis** - Optimize performance
5. **Server-Sent Events** - Implement real-time features

## 🏗️ Project Structure

Each project follows a similar structure:

```
project_name/
├── app/
│   ├── main.py           # FastAPI application entry point
│   ├── api/              # API route handlers
│   ├── models/           # Pydantic models or ORM models
│   ├── core/             # Core functionality (config, database, etc.)
│   ├── schemas/          # Request/response schemas
│   └── services/         # Business logic layer
├── .venv/                # Virtual environment
├── README.md             # Project-specific documentation
└── requirements.txt      # Python dependencies (if available)
```

## 🔑 Key Concepts Covered

- **RESTful API Design** - Proper HTTP methods, status codes, and resource naming
- **Dependency Injection** - FastAPI's powerful DI system
- **Data Validation** - Pydantic models for request/response validation
- **Async Programming** - Non-blocking I/O operations
- **Database Integration** - ORM patterns and raw SQL
- **Caching Strategies** - Performance optimization
- **Authentication & Authorization** - Securing APIs
- **Real-time Communication** - SSE and WebSocket alternatives
- **Error Handling** - Proper exception handling and responses
- **API Documentation** - Auto-generated OpenAPI/Swagger docs

## 🧪 Testing

Each project can be tested using:

- **Interactive Docs**: Navigate to `/docs` for Swagger UI
- **cURL**: Command-line HTTP requests
- **Postman/Insomnia**: API testing tools
- **pytest**: Unit and integration tests (where implemented)

Example cURL request:
```bash
curl -X GET "http://localhost:8000/endpoint" -H "accept: application/json"
```

## 📝 Best Practices Demonstrated

- ✅ Proper project structure and organization
- ✅ Environment-based configuration
- ✅ Dependency management
- ✅ Type hints and Pydantic validation
- ✅ Async/await for I/O operations
- ✅ Connection pooling and resource management
- ✅ Error handling and logging
- ✅ API versioning considerations
- ✅ Security best practices

## 🤝 Contributing

Feel free to:
- Add new demo projects
- Improve existing implementations
- Fix bugs or issues
- Enhance documentation
- Share feedback and suggestions

## 📚 Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Redis Documentation](https://redis.io/docs/)
- [Python Async/Await](https://docs.python.org/3/library/asyncio.html)

## 📄 License

This repository is for educational purposes. Feel free to use and modify the code for learning and development.

---

**Happy Learning! 🚀**

For project-specific details, refer to individual README files in each project directory.
