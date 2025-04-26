# Base image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWHRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essencial \ 
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Install dependencies
COPY pyproject.toml poetry.lock* /app/
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-root --no-interaction --no-ansi

# Copy project
COPY . /app/

# Expose the port the app runs on
EXPOSE 8000

#Command to run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app.wsgi:application"]