FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY framework/ ./framework/
COPY tests/ ./tests/
COPY pytest.ini .

RUN mkdir -p reports

CMD ["python", "-m", "pytest", "-v"]