FROM python:3.12-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir sqlalchemy alembic psycopg2-binary
CMD ["bash", "-c", "alembic upgrade head && python backend/scripts/seed.py && tail -f /dev/null"]
