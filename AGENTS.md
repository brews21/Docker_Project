# AGENTS.md

## Project Overview

This repository is for Docker-related files, including Dockerfiles, Compose
files, build contexts, examples, and supporting documentation.

## Working Guidelines

- Keep changes focused on Docker-related files and documentation.
- Do not commit secrets, tokens, credentials, private keys, or real production
  `.env` files.
- Prefer clear folder names such as `dockerfiles/`, `compose/`, and `examples/`
  when adding new material.
- Use lowercase, hyphenated names for Docker example directories and image
  examples when practical.
- Keep Dockerfiles readable: group related steps, avoid unnecessary layers, and
  add comments only when they explain a non-obvious choice.
- Prefer pinned base image tags over floating tags when reproducibility matters.
- Avoid destructive Docker commands such as broad image, volume, or system prune
  commands unless the user explicitly asks for cleanup.

## Verification

- For Dockerfiles, run the smallest relevant `docker build` when practical.
- For Compose files, run `docker compose config` before starting services when
  practical.
- Do not start long-running containers unless the user asks or it is necessary
  to verify the requested change.
