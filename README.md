# Development

Run backend:
```bash
cd backend
poetry install
docker run -p 6379:6379 -d redis:7-alpine
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
