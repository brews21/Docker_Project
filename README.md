# Docker Project

This repository contains multiple Docker project examples.

## Projects

- `flask_app/`: Docker image and Compose setup for a small Flask app.

## Flask App

Build an image:

```bash
docker build -t flask-docker-example:local -f flask_app/dockerfiles/flask-app.Dockerfile flask_app
```

Run a Compose stack:

```bash
docker compose -f flask_app/compose/docker-compose.yml up
```

The app listens on <http://localhost:5000>.

Stop and remove a Compose stack:

```bash
docker compose -f flask_app/compose/docker-compose.yml down
```

## Notes

- Avoid committing secrets, private keys, tokens, or local `.env` files.
- Prefer small, focused examples that are easy to build and inspect.
- Include comments in Dockerfiles when a step is non-obvious.
