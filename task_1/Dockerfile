FROM python:3.10.11-slim

ENV POETRY_VERSION=1.8.2
RUN pip install --no-cache-dir poetry==$POETRY_VERSION

WORKDIR /app

COPY pyproject.toml poetry.lock* /app/

RUN poetry config virtualenvs.create false \
 && poetry install --no-interaction --no-ansi

COPY . /app

CMD ["poetry", "run", "python", "main.py"]
