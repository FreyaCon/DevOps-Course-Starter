# base stage
FROM python:3.11-buster as base
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:${PATH}"
WORKDIR /todo_app
COPY poetry.toml pyproject.toml poetry.lock ./
RUN poetry install --no-root

EXPOSE 5000

# tests
FROM base AS test
ENV FLASK_APP=todo_app
ENV FLASK_DEBUG=true
COPY . /todo_app
ENTRYPOINT poetry run pytest

# dev
FROM base AS development
ENV FLASK_APP=todo_app
ENV FLASK_DEBUG=true
COPY . /todo_app
ENTRYPOINT poetry run flask run --host=0.0.0.0

#prod
FROM base AS production
ENV FLASK_APP=todo_app
ENV FLASK_DEBUG=false
COPY . /todo_app
ENTRYPOINT poetry run flask run --host=0.0.0.0
