## Requirements

Contact fields: first_name, last_name, email, phone, birthday, extra_data (optional).  
API: CRUD (create/list/get/update/delete), search by query params (first_name/last_name/email), birthdays next N days (default 7).  
Swagger available at `/docs`.

## Run PostgreSQL (Docker) — macOS / Windows

docker run --name goit-postgres-hw10 -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -d postgres

## Setup (venv + install)

macOS / Linux:
python3 -m venv .venv
source .venv/bin/activate

Windows (CMD / PowerShell):
python -m venv .venv
.venv\Scripts\activate

Then (both OS):
pip install --upgrade pip
pip install -r requirements.txt

## Environment (.env in project root)

DB_USER=postgres
DB_PASSWORD=mysecretpassword
DB_HOST=localhost
DB_PORT=5432
DB_NAME=postgres

## Alembic migrations (IMPORTANT: always run via python -m)

python -m alembic init migrations
python -m alembic revision --autogenerate -m "create contacts table"
python -m alembic upgrade head

## Run API (macOS / Windows)

uvicorn app.main:app --reload

## Swagger + Endpoints

Swagger: http://127.0.0.1:8000/docs
POST /api/contacts
GET /api/contacts?first_name=&last_name=&email=
GET /api/contacts/{id}
PUT /api/contacts/{id}
DELETE /api/contacts/{id}
GET /api/contacts/birthdays?days=7
