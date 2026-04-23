FROM python:3.11-slim

WORKDIR /app

RUN useradd -m appuser

# ✅ FIX: include path from root context
COPY api/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ✅ FIX: copy correct folder
COPY api/ .

USER appuser

EXPOSE 8000

HEALTHCHECK CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]