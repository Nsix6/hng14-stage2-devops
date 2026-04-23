FROM node:18-alpine

WORKDIR /app

# ✅ FIX: correct path from root context
COPY frontend/package*.json ./

# ✅ modern npm flag
RUN npm install --omit=dev

# ✅ copy only frontend app
COPY frontend/ .

EXPOSE 3000

CMD ["node", "app.js"]