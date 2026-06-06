# Docker Project

This repository contains Docker-related files, examples, and notes.

## Suggested Layout

```text
.
├── README.md
├── AGENTS.md
├── dockerfiles/
├── compose/
└── examples/
```

- `dockerfiles/`: standalone Dockerfiles or image build contexts.
- `compose/`: Docker Compose files for multi-container examples.
- `examples/`: sample apps, configs, or notes that support the Docker files.

## Common Commands

Build an image:

```bash
docker build -t image-name -f dockerfiles/Dockerfile .
```

Run a Compose stack:

```bash
docker compose -f compose/docker-compose.yml up
```

Stop and remove a Compose stack:

```bash
docker compose -f compose/docker-compose.yml down
```

## Notes

- Avoid committing secrets, private keys, tokens, or local `.env` files.
- Prefer small, focused examples that are easy to build and inspect.
- Include comments in Dockerfiles when a step is non-obvious.
