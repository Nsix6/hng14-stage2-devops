# hng14-stage2-devops

Overview

Distributed job processing system with:

Frontend (Node.js)
API (FastAPI)
Worker (Python)
Redis queue

# Requirements

Docker
Docker Compose
Node 18+
Python 3.11+

# Run

Within bash shell or any shell of preference

cp .env.example .env
docker-compose up --build

# Expected Behaviour

1. Open browser → http://localhost:3000
2. Click “Submit Job”
3. Job moves:
   - queued → processing → completed

# Architecture

Frontend -> API -> Redis -> Worker

# Health Checks

. Frontend /health
. API: /health
. Worker:internal

# Environment Variables

REDIS_HOST=redis
REDIS_PORT=6379
API_URL=http://api:8000
