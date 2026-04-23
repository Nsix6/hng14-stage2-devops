FROM python:3.11-slim

WORKDIR /app

RUN useradd -m appuser

# ✅ FIX: correct path
COPY worker/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ✅ FIX: copy worker folder
COPY worker/ .

USER appuser

CMD ["python", "worker.py"]