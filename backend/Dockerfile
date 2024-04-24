FROM python:3.12-alpine AS poetry
RUN pip install poetry
WORKDIR /poetry
COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt -o requirements.txt

FROM python:3.12-alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /backend
RUN echo ${PWD} && ls -lR
COPY --from=poetry /poetry/requirements.txt .
RUN pip install -r requirements.txt
COPY . .
