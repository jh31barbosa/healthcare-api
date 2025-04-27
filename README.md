# Healthcare Management API

API para gestão de profissionais de saúde e agendamento de consultas médicas.

## Tecnologias

- Python 3.9
- Django 4.2
- Django REST Framework
- PostgreSQL
- Docker
- Poetry (gerenciamento de dependências)

## Requisitos

- Docker e Docker Compose instalados
- Python 3.9+
- Poetry (opcional, mas recomendado)

## Configuração do Ambiente Local

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/healthcare-api.git
   cd healthcare-api

Crie um arquivo .env na raiz do projeto com as variáveis de ambiente:

POSTGRES_DB=healthcare_db
POSTGRES_USER=healthcare_user
POSTGRES_PASSWORD=healthcare_pass
POSTGRES_HOST=db
SECRET_KEY=sua-chave-secreta-aqui

Inicie os containers:
docker-compose up -d --build

Acesse o container e execute as migrações:
docker-compose exec web python manage.py migrate

Crie um superusuário (opcional):
docker-compose exec web python manage.py createsuperuser

A API estará disponível em: http://localhost:8000/api/

Rodando os Testes
docker-compose exec web python manage.py test

Rotas da API
Profissionais de Saúde: /api/professionals/

Consultas Médicas: /api/appointments/

Documentação Swagger disponível em: /api/swagger/

Deploy
O projeto está configurado para deploy contínuo no Digital Ocean via GitHub Actions.

Ambientes:
Staging: Automático a cada push na branch main

Production: Manual, acionado via GitHub Actions

Decisões Técnicas
Segurança:

Sanitização de inputs via Django REST Framework

Proteção contra SQL Injection usando ORM do Django

Validação de dados nos serializers

Performance:

Select related para evitar N+1 queries

Paginação padrão do DRF

Integração com Asaas:

Implementação mockada com possibilidade de integração real

Split de pagamento 70/30 entre profissional e plataforma