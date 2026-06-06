# Flask App

This project builds and runs a small Flask app image.

## Layout

```text
.
├── app/
├── compose/
├── dockerfiles/
└── README.md
```

- `app/`: Flask app and Python dependencies.
- `dockerfiles/`: Dockerfile for the Flask image.
- `compose/`: Compose file for running the app locally.

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

The app listens on <http://localhost:5000>.

Stop the app:

```bash
docker compose -f flask_app/compose/docker-compose.yml down
```
