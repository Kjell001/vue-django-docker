# Development

Run backend:
```bash
cd backend
poetry install
docker run -p 6379:6379 -d redis:7-alpine
export POSTGRES_PASSWORD=poppin_kernels
docker run -p 5432:5432 -e POSTGRES_PASSWORD=$POSTGRES_PASSWORD -d postgres:16-alpine
poetry run python manage.py migrate
poetry run python manage.py seed
poetry run python manage.py runserver
```

Run frontend:
```bash
cd frontend
yarn install
yarn dev
```

# Docker

```bash
docker compose down -v
docker compose up --build --force-recreate -d
```
