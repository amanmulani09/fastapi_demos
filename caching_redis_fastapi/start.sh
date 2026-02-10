#!/bin/bash

# Check if Redis is installed
if ! command -v redis-server &> /dev/null; then
    echo "Redis is not installed. Installing via Homebrew..."
    brew install redis
fi

# Check if Redis is already running
if ! redis-cli ping &> /dev/null; then
    echo "Starting Redis..."
    brew services start redis
    
    # Wait for Redis to be ready
    echo "Waiting for Redis to be ready..."
    until redis-cli ping &> /dev/null; do
        echo "Redis is unavailable - sleeping"
        sleep 1
    done
    echo "Redis is up and running!"
else
    echo "Redis is already running!"
fi

# Activate virtual environment if it exists
if [ -d ".venv" ]; then
    echo "Activating virtual environment..."
    source .venv/bin/activate
fi

# Start FastAPI application
echo "Starting FastAPI application..."
cd app && uvicorn main:app --reload --host 0.0.0.0 --port 8000
