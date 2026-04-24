# Stage 1: build
FROM node:18-alpine AS builder

WORKDIR /app

COPY package*.json ./

# ✅ FIX HERE
RUN npm install --legacy-peer-deps

COPY . .

# Stage 2: runtime
FROM node:18-alpine

WORKDIR /app

RUN adduser -D appuser

COPY --from=builder /app /app

USER appuser

EXPOSE 3000

HEALTHCHECK CMD wget -qO- http://localhost:3000/health || exit 1

CMD ["node", "app.js"]