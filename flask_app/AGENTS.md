# AGENTS.md

## Project Overview

This folder contains the Flask app Docker project, including the Flask image,
Nginx reverse proxy image, and Compose setup.

## Docker Access

- Docker daemon access is approved for this project when needed to build,
  inspect, run, or stop the Flask/Nginx containers.
- If the execution environment still requires an explicit approval prompt for
  Docker daemon access, request it and continue verification after approval.
- Do not run destructive Docker cleanup commands such as broad image, volume, or
  system prune commands unless the user explicitly asks for cleanup.

## Verification

- Run `docker compose -f flask_app/compose/docker-compose.yml config` from the
  repository root after Compose changes.
- Run the smallest relevant `docker build` or `docker compose up -d --build`
  check when changing Dockerfiles, app runtime behavior, or Nginx proxy config.
- Stop any temporary containers started for verification before finishing.
