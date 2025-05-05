FROM ghcr.io/astral-sh/uv:python3.12-alpine

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync --locked

COPY . .

EXPOSE 8000

CMD ["uv", "run", "config.asgi:application", "--host", "0.0.0.0", "--port", "8000"]