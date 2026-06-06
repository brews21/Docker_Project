# Flask App

This project builds and runs a small Flask app image behind Nginx.

## Layout

```text
.
├── app/
├── compose/
├── dockerfiles/
├── nginx/
└── README.md
```

- `app/`: Flask app and Python dependencies.
- `dockerfiles/`: Dockerfiles for the Flask and Nginx images.
- `compose/`: Compose file for running the app locally.
- `nginx/`: Nginx reverse proxy configuration.

## Build

From the repository root:

```bash
docker build -t flask-docker-example:local -f flask_app/dockerfiles/flask-app.Dockerfile flask_app
```

## Run

From the repository root:

```bash
docker compose -f flask_app/compose/docker-compose.yml up
```

Nginx listens on <http://localhost:8080> and proxies to the Flask app.

Stop the app:

```bash
docker compose -f flask_app/compose/docker-compose.yml down
```
