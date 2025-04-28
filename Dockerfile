FROM python:3.9-slim

# Configuração do ambiente
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH="/venv/bin:$PATH"

# Instala dependências do sistema
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev && \
    rm -rf /var/lib/apt/lists/*

# Cria e ativa venv
RUN python -m venv /venv
ENV VIRTUAL_ENV=/venv

# Instala dependências Python
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN pip install --upgrade pip && \
    pip install poetry gunicorn && \
    poetry install --only main --no-interaction --no-ansi

# Copia o projeto
COPY . .

# Coleta static files (Django)
RUN python manage.py collectstatic --noinput

# Configura o comando de execução
CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "app.wsgi:application"]