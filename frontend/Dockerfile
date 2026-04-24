FROM node:18-alpine

WORKDIR /app

COPY frontend/package*.json ./
RUN npm install --omit=dev --legacy-peer-deps

COPY frontend/ .

CMD ["node", "app.js"]