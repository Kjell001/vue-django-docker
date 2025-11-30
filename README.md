# Development

Prepare repository
```bash
cd frontend
yarn hooks
```

Run backend:
```bash
cd backend
# Install dependencies
uv sync
# Run redis and postgres containers
docker run -p 6379:6379 -d --name dev-redis redis:8-alpine 
export POSTGRES_PASSWORD=poppin_kernels
docker run -p 5432:5432 -e POSTGRES_PASSWORD=$POSTGRES_PASSWORD -d --name dev-postgres postgres:18-alpine 
# Set up database
uv run python manage.py migrate
uv run python manage.py seed
# Run server
uv run python manage.py runserver
```

Run frontend:
```bash
cd frontend
yarn install
yarn dev
```

# Docker

```bash
docker compose down
docker compose up --wait
```

Access frontend via 
```bash
http://localhost:3000
```

Access backend via 
```bash
http://localhost:8000
```