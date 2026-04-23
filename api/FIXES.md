# Fixes and Improvements Log

## Initial Bugs / Issues

1. **Hardcoded Redis connection**
   - Original code used `localhost:6379` directly.
   - Problem: In Docker Compose, `localhost` refers to the container itself, not the Redis service.
   - Result: Backend could not connect to Redis when containerized.

2. **No health check endpoint**
   - Original code had no `/health` route.
   - Problem: Could not easily verify if the API service was alive.
   - Result: Harder to monitor or orchestrate containers.

3. **Redis responses returned as raw bytes**
   - Without `decode_responses=True`, Redis returned byte strings.
   - Problem: Required manual `.decode()` calls, error‑prone and inconsistent.

## Improvements Made

1. **Configurable Redis connection**
   - Added environment variable support for `REDIS_HOST` and `REDIS_PORT`.
   - Defaults to `redis:6379` for Docker Compose.
   - Fixes networking bug and allows flexible configuration.

2. **Decode Redis responses**
   - Added `decode_responses=True` to Redis client.
   - Simplifies code by returning strings directly.

3. **Health endpoint**
   - Added `/health` route returning `{status: "ok"}`.
   - Provides a simple way to check if the API service is running.

## Current State

- Backend now works both locally and in Docker.
- Redis connection is configurable and robust.
- Health endpoint supports monitoring and orchestration.
- Error handling remains minimal, but critical Dockerization issues are resolved.
