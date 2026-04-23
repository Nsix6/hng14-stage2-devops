# Fixes and Improvements Log

## Initial Bugs / Issues

1. **Hardcoded API URL**
   - Defaulted to `http://localhost:8000`.
   - Problem: In Docker Compose, `localhost` refers to the container itself, not the backend service.
   - Result: Frontend could not reach API when containerized.

2. **No timeout on API requests**
   - Axios calls could hang indefinitely if API was down.
   - Result: Poor user experience, no clear error feedback.

3. **Generic error handling**
   - Returned `500 Internal Server Error` for all failures.
   - Did not log error details.
   - Result: Hard to debug API connectivity issues.

4. **No health check endpoint**
   - Could not easily verify frontend was running.
   - Result: Harder to monitor in production.

## Improvements Made

1. **API URL default changed**
   - Now defaults to `http://api:8000`.
   - Fixes container networking bug by using service name.

2. **Reusable Axios client**
   - Created with `baseURL` and `timeout`.
   - Cleaner code, prevents hanging requests.

3. **Improved error handling**
   - Logs error messages to console.
   - Returns `502 Bad Gateway` to indicate upstream API issues.

4. **Added health endpoint**
   - `/health` returns `{ status: "ok" }`.
   - Useful for monitoring and orchestration.

5. **Consistency and clarity**
   - Unified error responses.
   - Explicit empty payload in `/submit`.
   - Cleaner code style with single quotes.

## Current State

- Frontend now works both locally and in Docker.
- Requests fail fast with clear error messages if API is unavailable.
- Health endpoint allows easy monitoring.
- Code is cleaner, more maintainable, and production-ready.
