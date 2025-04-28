 Healthcare Management API


Um sistema completo para gerenciamento de profissionais de saúde e agendamento de consultas médicas, desenvolvido com Django REST Framework e Docker, pronto para deploy na DigitalOcean ou AWS.

📌 Sumário
Visão Geral

Funcionalidades

Tecnologias

Pré-requisitos

Configuração Local

Deploy na DigitalOcean

Rotas da API

Testes

Contribuição

Licença

🌟 Visão Geral
Esta API permite:

✅ Cadastro e gerenciamento de profissionais de saúde

✅ Agendamento de consultas médicas

✅ Filtros e buscas avançadas

✅ Segurança e validação de dados

🛠 Funcionalidades
Profissionais de Saúde
CRUD completo (Create, Read, Update, Delete)

Filtros por profissão, nome e contato

Consultas Médicas
Agendamento com vínculo ao profissional

Filtros por data e profissional

Segurança
Sanitização de inputs

Proteção contra SQL Injection

💻 Tecnologias

Tecnologia	Descrição
Python 3.11	Linguagem principal
Django	Framework web
Django REST	Construção de APIs RESTful
PostgreSQL	Banco de dados principal
Docker	Containerização da aplicação
Gunicorn	Servidor WSGI para produção
Poetry	Gerenciamento de dependências
GitHub Actions	CI/CD automatizado
📋 Pré-requisitos
Docker (Instalação)

Docker Compose (Instalação)

Python 3.11+ (Download)

Conta na DigitalOcean (para deploy)

🚀 Configuração Local
1. Clone o repositório
bash
Copy
Edit
git clone https://github.com/jh29dev/healthcare-api.git
cd healthcare-api
2. Configure as variáveis de ambiente
Crie um arquivo .env na raiz do projeto:

ini
Copy
Edit
# Django
SECRET_KEY=sua-chave-secreta
DEBUG=True

# Banco de dados
POSTGRES_DB=healthcare_db
POSTGRES_USER=healthcare_user
POSTGRES_PASSWORD=healthcare_pass
POSTGRES_HOST=db
POSTGRES_PORT=5432
3. Inicie os containers
bash
Copy
Edit
docker compose up -d --build
4. Aplique as migrações
bash
Copy
Edit
docker compose exec web python manage.py migrate
5. Crie um superusuário (opcional)
bash
Copy
Edit
docker compose exec web python manage.py createsuperuser
6. Acesse a aplicação
API: http://localhost:8000/api/

Admin: http://localhost:8000/admin/

☁ Deploy na DigitalOcean
1. Pré-requisitos
Conta na DigitalOcean

Container Registry configurado

App Platform ativado

2. Configuração do GitHub Actions
Adicione os secrets no repositório (Settings > Secrets > Actions):

DIGITALOCEAN_ACCESS_TOKEN

DB_HOST

DB_PASSWORD

3. Fluxo de Deploy Automático
Push na branch main dispara o CI/CD

Build e deploy automático na DigitalOcean

📡 Rotas da API
Profissionais de Saúde
GET /api/professionals/ → Lista todos

POST /api/professionals/ → Cria novo

GET /api/professionals/{id}/ → Detalhes

Consultas Médicas
GET /api/appointments/ → Lista todas

POST /api/appointments/ → Agenda nova

GET /api/appointments/?professional_id=1 → Filtra por profissional

🧪 Testes
Execute os testes com:

bash
Copy
Edit
docker compose exec web python manage.py test
🤝 Contribuição
Faça um fork do projeto

Crie uma nova branch:

bash
Copy
Edit
git checkout -b feature/nova-funcionalidade
Commit suas alterações:

bash
Copy
Edit
git commit -m "Adiciona nova funcionalidade"
Faça push para o branch:

bash
Copy
Edit
git push origin feature/nova-funcionalidade
Abra um Pull Request

📜 Licença
Distribuído sob a licença MIT.
Consulte o arquivo LICENSE para mais informações.

