# FastAPI Redis Caching Demo

A FastAPI application demonstrating Redis caching implementation.

## Prerequisites

- Python 3.8+
- Homebrew (for macOS)
- Redis (will be installed automatically if not present)

## Quick Start

### Automated Startup (Recommended)

Simply run the start script which will:
1. Check if Redis is installed (installs if needed)
2. Start Redis service
3. Activate virtual environment
4. Start FastAPI application

```bash
./start.sh
```

The application will be available at `http://localhost:8000`

### Stop Services

```bash
./stop.sh
```

## Manual Setup

### 1. Install Redis (if not already installed)

```bash
brew install redis
```

### 2. Start Redis

```bash
# Start as a background service (persists across reboots)
brew services start redis

# Or run in foreground (stops when terminal closes)
redis-server
```

### 3. Verify Redis is Running

```bash
redis-cli ping
# Should return: PONG
```

### 4. Start FastAPI Application

```bash
# Activate virtual environment
source .venv/bin/activate

# Start the application
cd app && uvicorn main:app --reload
```

## API Endpoints

- `GET /users/{user_id}` - Get user by ID (with caching)
- `POST /users` - Create a new user
- `DELETE /users/{user_id}` - Delete user and invalidate cache

## Testing the Cache

```bash
# First request - cache miss (slower)
curl http://localhost:8000/users/1

# Second request - cache hit (faster)
curl http://localhost:8000/users/1

# Check response headers to see cache status
curl -i http://localhost:8000/users/1
```

## Environment Variables

Create a `.env` file in the root directory (optional):

```env
APP_NAME=FastAPI Redis Cache
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0
```

## Redis Management Commands

```bash
# Check Redis status
brew services list | grep redis

# Stop Redis
brew services stop redis

# Restart Redis
brew services restart redis

# Connect to Redis CLI
redis-cli

# View all keys in Redis
redis-cli KEYS "*"

# Flush all cache data
redis-cli FLUSHALL
```

## Troubleshooting

### Connection Refused Error

If you see `[Errno 61] Connect call failed ('127.0.0.1', 6379)`:

1. **Check if Redis is running:**
   ```bash
   brew services list | grep redis
   ```

2. **Start Redis:**
   ```bash
   brew services start redis
   ```

3. **Verify connection:**
   ```bash
   redis-cli ping
   ```

### Redis Not Installed

```bash
brew install redis
brew services start redis
```

### Port Already in Use

If port 6379 is already in use:

```bash
# Find process using port 6379
lsof -i :6379

# Kill the process if needed
kill -9 <PID>

# Restart Redis
brew services restart redis
```

## Project Structure

```
caching_redis_fastapi/
├── app/
│   ├── main.py              # FastAPI application with lifespan
│   ├── api/
│   │   └── users.py         # User endpoints
│   ├── cache/
│   │   └── cache_service.py # Redis cache service
│   ├── core/
│   │   ├── config.py        # Configuration settings
│   │   └── redis.py         # Redis connection management
│   └── models/
│       └── user.py          # User model
├── start.sh                 # Automated startup script
├── stop.sh                  # Stop Redis service
└── README.md               # This file
```

## How It Works

1. **Application Startup**: The FastAPI lifespan context manager initializes Redis connection
2. **Cache Check**: When a user is requested, the cache is checked first
3. **Cache Miss**: If not in cache, data is fetched and stored in Redis with TTL
4. **Cache Hit**: Subsequent requests return cached data instantly
5. **Cache Invalidation**: Deleting a user removes it from cache
