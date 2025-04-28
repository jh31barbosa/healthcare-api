FROM python:3.11-slim  # Mudei para 3.11 (mais estável) e slim (mais leve)

# Configuração do ambiente
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH="/venv/bin:$PATH" \
    POETRY_VERSION=1.7.0

# Instala dependências mínimas do sistema
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Instala Poetry explicitamente
RUN pip install --no-cache-dir "poetry==$POETRY_VERSION"

# Configura o ambiente virtual
WORKDIR /app
RUN python -m venv /venv

# Copia apenas os arquivos necessários para instalação
COPY pyproject.toml poetry.lock ./

# Instala dependências
RUN poetry install --only main --no-interaction --no-ansi

# Copia o restante do projeto
COPY . .

# Coleta static files
RUN python manage.py collectstatic --noinput

# Configura o comando de execução
CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "app.wsgi:application"]