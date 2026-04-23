FROM node:18-alpine

WORKDIR /app

COPY frontend/package*.json ./

RUN npm install --omit=dev --legacy-peer-deps

COPY frontend/ .

EXPOSE 3000

CMD ["node", "app.js"]