FROM python:3.11-slim

WORKDIR /app

RUN useradd -m appuser

COPY worker/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY worker/ .

USER appuser

CMD ["python", "worker.py"]